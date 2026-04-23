#!/opt/homebrew/bin/python3
"""
Daily Pipeline Review Cron — Richie
Sends to Marrs via OpenClaw message system
"""
import os, sys, json
sys.path.insert(0, os.path.expanduser("~/.config/richie-google"))

# Import the review generator
exec(open(os.path.expanduser("~/.openclaw/workspace/scripts/pipeline-review.py")).read().replace("if __name__ == '__main__':", "if False:"))

# Generate review
review = generate_review()

# Save to shared location for delivery
output_file = os.path.expanduser("~/.openclaw/workspace/reports/daily-pipeline-latest.txt")
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as f:
    f.write(review)

print(f"Review saved to {output_file}")
print(review)
