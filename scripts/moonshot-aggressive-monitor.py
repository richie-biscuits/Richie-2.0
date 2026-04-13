#!/usr/bin/env python3
"""
Moonshot Aggressive Monitor - BTC Trading Signal Generator & Executor
Monitors RSI signals, executes trades on Kraken, reports to Telegram.
Designed to be aggressive but risk-managed.
"""

import json
import time
import hmac
import hashlib
import base64
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from enum import Enum

# ============================================================================
# CONFIGURATION
# ============================================================================

# Kraken API credentials - stored in environment or config
KRAKEN_API_KEY = ""  # Add your API key
KRAKEN_API_SECRET = ""  # Add your API secret

# Telegram
TELEGRAM_BOT_TOKEN = ""  # Add your bot token
TELEGRAM_CHAT_ID = ""  # Add your chat ID

# Trading parameters
RSI_PERIOD = 14
RSI_OVERSOLD = 35        # BUY signal threshold (RSI below this = oversold = accumulation opportunity)
RSI_OVERBOUGHT = 70      # SELL signal threshold (RSI above this = overbought = distribution)
RSI_STRONG = 25          # Strong signal threshold - extreme oversold (BUY) or overbought (SELL)
TRADE_AMOUNT_USD = 100   # Default trade size in USD
MAX_POSITION_SIZE = 500  # Maximum position in USD

# Supabase (for logging)
SUPABASE_URL = "https://cmqzawbdtnkynizughqq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtcXphd2JkdG5reW5penVnaHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NzI1MTQsImV4cCI6MjA4ODI0ODUxNH0.Ha0-nnKHmCPBbfHYaebCcbjmeKZLrXYfGxTjuVlmLw8"

class SignalUrgency(Enum):
    HIGH = "HIGH"      # Execute trade automatically
    MEDIUM = "MEDIUM"  # Report to Telegram, no auto-execute
    LOW = "LOW"        # Log only
    NONE = "NONE"      # No signal

def log_to_supabase(trade_data):
    """Log trade signals to Supabase."""
    try:
        import urllib.request
        data = json.dumps(trade_data).encode('utf-8')
        req = urllib.request.Request(
            f"{SUPABASE_URL}/rest/v1/trades",
            data=data,
            headers={
                'Content-Type': 'application/json',
                'apikey': SUPABASE_KEY,
                'Authorization': f'Bearer {SUPABASE_KEY}',
                'Prefer': 'return=minimal'
            },
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 201 or response.status == 200
    except Exception as e:
        print(f"Failed to log to Supabase: {e}")
        return False

def send_telegram(message):
    """Send message to Telegram."""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram not configured - skipping notification")
        return False
    
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = urllib.parse.urlencode({
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }).encode('utf-8')
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200
    except Exception as e:
        print(f"Failed to send Telegram: {e}")
        return False

def kraken_request(endpoint, data=None, api_key=None, api_secret=None):
    """Make authenticated request to Kraken API."""
    if data is None:
        data = {}
    
    # Add nonce
    nonce = str(int(time.time() * 1000))
    data['nonce'] = nonce
    
    # Encode data
    postdata = urllib.parse.urlencode(data)
    
    # Create signature
    if api_key and api_secret:
        # Kraken signature creation
        message = endpoint.encode('utf-8') + hashlib.sha256((nonce + postdata).encode('utf-8')).digest()
        signature = hmac.new(
            base64.b64decode(api_secret),
            message,
            hashlib.sha512
        ).digest()
        
        headers = {
            'API-Key': api_key,
            'API-Sign': base64.b64encode(signature).decode('utf-8'),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    else:
        headers = {}
    
    url = f"https://api.kraken.com{endpoint}"
    req = urllib.request.Request(url, data=postdata.encode('utf-8'), headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        return {'error': [str(e)]}

def get_btc_price():
    """Get current BTC/USD price - tries multiple sources."""
    # Try CoinGecko first (most reliable)
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            return float(data['bitcoin']['usd'])
    except Exception as e:
        print(f"CoinGecko failed: {e}")
    
    # Fallback: Kraken
    try:
        url = "https://api.kraken.com/public/ticker?pair=XBTUSD"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if 'error' not in data or not data['error']:
                for key in data.get('result', {}).keys():
                    if 'XBT' in key or 'BTC' in key:
                        return float(data['result'][key]['c'][0])
    except Exception as e:
        print(f"Kraken ticker failed: {e}")
    
    # Fallback: Coinbase
    try:
        url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            return float(json.loads(response.read().decode('utf-8'))['data']['amount'])
    except Exception as e:
        print(f"Coinbase failed: {e}")
    
    return None

def get_btc_klines(interval=1, count=100):
    """Get BTC klines/candles for RSI calculation - tries multiple sources."""
    # Try Binance first
    try:
        url = f"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit={count}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            # Format: [open time, open, high, low, close, volume, close time, ...]
            return [[float(k[4])] for k in data]  # Return just close prices wrapped
    except Exception as e:
        print(f"Binance klines failed: {e}")
    
    # Try Kraken
    try:
        interval_map = {1: 1, 5: 5, 15: 15, 60: 60}
        kraken_interval = interval_map.get(interval, 1)
        url = f"https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval={kraken_interval}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if 'error' in data and data['error']:
                return []
            result = data.get('result', {})
            for key in result.keys():
                if 'XBT' in key or 'BTC' in key:
                    return result[key]
            return []
    except Exception as e:
        print(f"Kraken klines failed: {e}")
    
    return []

def calculate_rsi(prices, period=14):
    """Calculate RSI indicator."""
    if len(prices) < period + 1:
        return None
    
    deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    
    if avg_loss == 0:
        return 100
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return round(rsi, 2)

def get_market_summary():
    """Get comprehensive market summary."""
    price = get_btc_price()
    klines = get_btc_klines(interval=1, count=50)  # 1-minute candles
    
    if not price:
        return None
    
    # Use closes from price if klines is empty or small
    if klines and len(klines) > 0:
        first = klines[0]
        if isinstance(first, list):
            if len(first) == 1:
                # Our wrapped format: [[price1], [price2], ...] or Binance raw
                # Check if it looks like prices or OHLC
                try:
                    val = float(first[0])
                    if val > 1000:  # Likely a price
                        closes = [float(k[0]) for k in klines]
                    else:
                        closes = [price]
                except:
                    closes = [price]
            elif len(first) == 5 or len(first) == 6:
                # Binance format: [open_time, open, high, low, close, volume, ...]
                closes = [float(k[4]) for k in klines]
            elif len(first) > 4:
                # Kraken format: [time, open, high, low, close, volume, ...]
                closes = [float(k[4]) for k in klines]
            else:
                closes = [price]
        else:
            closes = [float(k) for k in klines]
    else:
        closes = [price]
    
    rsi_14 = calculate_rsi(closes, 14) if len(closes) >= 15 else None
    rsi_7 = calculate_rsi(closes[-7:], 7) if len(closes) >= 8 else None
    
    # Calculate recent momentum
    if len(closes) >= 5:
        momentum_5m = ((closes[-1] - closes[-5]) / closes[-5]) * 100
    else:
        momentum_5m = 0
    
    if len(closes) >= 20:
        momentum_20m = ((closes[-1] - closes[-20]) / closes[-20]) * 100
    else:
        momentum_20m = 0
    
    return {
        'price': price,
        'rsi_14': rsi_14,
        'rsi_7': rsi_7,
        'momentum_5m': round(momentum_5m, 3),
        'momentum_20m': round(momentum_20m, 3),
        'closes': closes[-30:]  # Last 30 closes for reference
    }

def determine_signal(market_data):
    """Determine trading signal based on RSI and momentum.
    
    RSI interpretation (inverted from traditional for this strategy):
    - LOW RSI (< 35) = Oversold = BUY opportunity (this is an aggressive accumulator)
    - HIGH RSI (> 70) = Overbought = SELL opportunity
    
    The strategy is: buy when others are fearful (low RSI), sell when greedy (high RSI).
    """
    if not market_data or not market_data.get('price'):
        return SignalUrgency.NONE, None
    
    rsi = market_data.get('rsi_14') or 50
    momentum = market_data.get('momentum_5m', 0)
    price = market_data['price']
    
    signal_details = {
        'rsi': rsi,
        'momentum': momentum,
        'price': price,
        'action': 'HOLD'
    }
    
    # BUY SIGNALS (RSI low = oversold = accumulation opportunity)
    
    # Strong buy - RSI below 25, deeply oversold - accumulate aggressively
    if rsi < RSI_STRONG:
        signal_details['action'] = 'STRONG_BUY'
        signal_details['reason'] = f'RSI {rsi} deeply oversold - accumulate'
        return SignalUrgency.HIGH, signal_details
    
    # Oversold - RSI below 35, potential buy opportunity
    if rsi < RSI_OVERSOLD:
        if momentum > 0.5:  # Also showing positive momentum = confirmation
            signal_details['action'] = 'BUY'
            signal_details['reason'] = f'RSI {rsi} oversold with +momentum {momentum}%'
            return SignalUrgency.HIGH, signal_details
        elif rsi < 30:
            signal_details['action'] = 'BUY'
            signal_details['reason'] = f'RSI {rsi} deeply oversold'
            return SignalUrgency.HIGH, signal_details
        else:
            signal_details['action'] = 'BUY_WATCH'
            signal_details['reason'] = f'RSI {rsi} oversold, waiting confirmation'
            return SignalUrgency.MEDIUM, signal_details
    
    # SELL SIGNALS (RSI high = overbought = distribution opportunity)
    
    # Strong sell - RSI above 75, extremely overbought - take profit
    if rsi > 75:
        signal_details['action'] = 'STRONG_SELL'
        signal_details['reason'] = f'RSI {rsi} extremely overbought - take profit'
        return SignalUrgency.HIGH, signal_details
    
    # Overbought - RSI above 70, potential sell
    if rsi > RSI_OVERBOUGHT:
        signal_details['action'] = 'SELL'
        signal_details['reason'] = f'RSI {rsi} overbought'
        return SignalUrgency.MEDIUM, signal_details  # MEDIUM for regular overbought
    
    # WATCH signals - RSI approaching extremes but not there yet
    if rsi < 40:
        signal_details['action'] = 'BUY_WATCH'
        signal_details['reason'] = f'RSI {rsi} neutral-low, watching for entry'
        return SignalUrgency.LOW, signal_details
    
    if rsi > 65:
        signal_details['action'] = 'SELL_WATCH'
        signal_details['reason'] = f'RSI {rsi} neutral-high, watching for exit'
        return SignalUrgency.LOW, signal_details
    
    # No signal
    return SignalUrgency.NONE, signal_details

def execute_trade(action, market_data, dry_run=True):
    """Execute trade on Kraken (or dry run).
    
    Actions:
    - BUY / STRONG_BUY: Market buy BTC
    - SELL / STRONG_SELL: Market sell BTC
    - BUY_WATCH / SELL_WATCH: No trade, just watch
    """
    # No trade for watch actions
    if 'WATCH' in action or action == 'HOLD':
        return {'dry_run': True, 'action': action, 'price': market_data['price'], 'skipped': True}
    
    if not KRAKEN_API_KEY or dry_run:
        print(f"[DRY RUN] Would execute: {action} at ${market_data['price']}")
        return {'dry_run': True, 'action': action, 'price': market_data['price']}
    
    pair = "XXBTZUSD"  # Kraken BTC/USD
    volume_btc = str(TRADE_AMOUNT_USD / market_data['price'])
    
    if 'BUY' in action:  # BUY or STRONG_BUY
        result = kraken_request(
            "/0/private/AddOrder",
            {
                'pair': pair,
                'type': 'buy',
                'ordertype': 'market',
                'volume': volume_btc,
                'validate': 'false'
            },
            KRAKEN_API_KEY,
            KRAKEN_API_SECRET
        )
        return result
    
    elif 'SELL' in action:  # SELL or STRONG_SELL
        result = kraken_request(
            "/0/private/AddOrder",
            {
                'pair': pair,
                'type': 'sell',
                'ordertype': 'market',
                'volume': volume_btc,
                'validate': 'false'
            },
            KRAKEN_API_KEY,
            KRAKEN_API_SECRET
        )
        return result
    
    return {'error': 'Unknown action'}

def format_report(market_data, signal, urgency, timestamp):
    """Format trading signal report."""
    emoji = {
        'HIGH': '🚨',
        'MEDIUM': '⚠️',
        'LOW': '📊',
        'NONE': '➖'
    }.get(urgency, '❓')
    
    action_emoji = {
        'BUY': '🟢',
        'STRONG_BUY': '🟢🟢',
        'SELL': '🔴',
        'STRONG_SELL': '🔴🔴',
        'BUY_WATCH': '👀🟢',
        'SELL_WATCH': '👀🔴',
        'WATCH': '👀',
        'HOLD': '⏸️'
    }.get(signal.get('action', 'HOLD'), '❓')
    
    report = f"""
{emoji} <b>MOONSHOT AGGRESSIVE MONITOR</b> {emoji}
━━━━━━━━━━━━━━━━━━━━
🕐 {timestamp}

💰 <b>BTC Price:</b> ${market_data['price']:,.2f}

📈 <b>Indicators:</b>
   RSI(14): {market_data.get('rsi_14', 'N/A')}
   RSI(7): {market_data.get('rsi_7', 'N/A')}
   Momentum 5m: {market_data.get('momentum_5m', 0):+.3f}%
   Momentum 20m: {market_data.get('momentum_20m', 0):+.3f}%

{action_emoji} <b>Signal:</b> {signal.get('action', 'HOLD')}
   {signal.get('reason', 'No specific reason')}

📊 <b>Urgency:</b> {urgency}
"""
    
    return report

def main():
    """Main monitor loop."""
    print("=" * 60)
    print("MOONSHOT AGGRESSIVE MONITOR - Starting")
    print("=" * 60)
    
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    print(f"Timestamp: {timestamp}")
    
    # Get market data
    print("\n[1/3] Fetching market data...")
    market_data = get_market_summary()
    
    if not market_data:
        print("ERROR: Could not fetch market data")
        send_telegram("🚨 <b>Moonshot Monitor Error</b>\n\nFailed to fetch BTC market data. Check API connectivity.")
        return
    
    print(f"   BTC Price: ${market_data['price']:,.2f}")
    print(f"   RSI(14): {market_data.get('rsi_14', 'N/A')}")
    print(f"   Momentum 5m: {market_data.get('momentum_5m', 0):+.3f}%")
    
    # Determine signal
    print("\n[2/3] Analyzing signals...")
    urgency, signal = determine_signal(market_data)
    print(f"   Action: {signal.get('action', 'HOLD')}")
    print(f"   Reason: {signal.get('reason', 'N/A')}")
    print(f"   Urgency: {urgency.value}")
    
    # Format and send report
    print("\n[3/3] Generating report...")
    report = format_report(market_data, signal, urgency.value, timestamp)
    print(report)
    
    # Log to Supabase
    log_entry = {
        'timestamp': timestamp,
        'price': market_data['price'],
        'rsi_14': market_data.get('rsi_14'),
        'rsi_7': market_data.get('rsi_7'),
        'momentum_5m': market_data.get('momentum_5m'),
        'momentum_20m': market_data.get('momentum_20m'),
        'action': signal.get('action', 'HOLD'),
        'reason': signal.get('reason', ''),
        'urgency': urgency.value,
        'created_at': datetime.now(timezone.utc).isoformat()
    }
    log_to_supabase(log_entry)
    
    # Handle based on urgency
    if urgency == SignalUrgency.HIGH:
        print("\n⚡ HIGH URGENCY - Executing trade...")
        result = execute_trade(signal.get('action', 'BUY'), market_data, dry_run=True)
        
        if result.get('dry_run'):
            print(f"   [DRY RUN] Trade simulation complete")
            report += "\n\n⚡ <b>TRADE EXECUTED (DRY RUN)</b>"
        else:
            if 'error' in result:
                report += f"\n\n❌ <b>Trade Failed:</b> {result['error']}"
            else:
                report += "\n\n✅ <b>Trade Executed Successfully</b>"
        
        # Always notify for HIGH
        send_telegram(report)
        
    elif urgency == SignalUrgency.MEDIUM:
        print("\n⚠️ MEDIUM URGENCY - Reporting to Telegram...")
        send_telegram(report)
    
    else:
        print("\n➖ No urgent action required")
        # Optional: send periodic heartbeat
        # send_telegram(report)
    
    print("\n" + "=" * 60)
    print("MOONSHOT AGGRESSIVE MONITOR - Complete")
    print("=" * 60)

if __name__ == "__main__":
    main()