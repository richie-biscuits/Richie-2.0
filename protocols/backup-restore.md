# Backup & Restore Protocol

## Purpose
Ensure business continuity and data integrity for OpenClaw + Polynize Labs operations.

## Daily Backups

### 1. Git Workspace Backup (Automated)
- **Schedule:** Every 6 hours via cron job
- **Scope:** `/Users/openclaw_admin/.openclaw/workspace`
- **Process:**
  1. Check git status for changes
  2. Stage all changes
  3. Commit with timestamp: `Auto backup: YYYY-MM-DD HH:MM`
  4. Push to origin/main
- **Verification:** Check GitHub repository for latest commit

### 2. Configuration Backup (Manual - Weekly)
- **Scope:**
  - `/Users/openclaw_admin/.openclaw/openclaw.json`
  - `/Users/openclaw_admin/.openclaw/cron/jobs.json`
  - `/Users/openclaw_admin/.openclaw/agents/main/agent/auth-profiles.json`
- **Process:**
  1. Copy files to `/Users/openclaw_admin/.openclaw/backups/config-YYYY-MM-DD/`
  2. Encrypt sensitive files (auth profiles)
  3. Commit to git with `[Config Backup]` prefix

### 3. Scripts Backup (On Change)
- **Scope:** `/Users/openclaw_admin/.openclaw/scripts/`
- **Process:** Git commit when scripts are modified

## Disaster Recovery

### Scenario 1: Workspace Corruption/Loss
**Recovery Steps:**
1. Clone repository from GitHub:
   ```bash
   git clone https://github.com/[username]/[repo].git /Users/openclaw_admin/.openclaw/workspace
   ```
2. Restore configuration files from latest backup
3. Verify cron jobs are running
4. Test agent functionality

### Scenario 2: OpenClaw Installation Failure
**Recovery Steps:**
1. Reinstall OpenClaw:
   ```bash
   npm install -g openclaw
   ```
2. Restore configuration:
   ```bash
   cp /Users/openclaw_admin/.openclaw/backups/config-latest/openclaw.json ~/.openclaw/
   ```
3. Restart gateway:
   ```bash
   openclaw gateway restart
   ```
4. Verify agent connectivity

### Scenario 3: Complete System Loss
**Recovery Steps:**
1. Provision new machine (macOS/Linux)
2. Install prerequisites:
   ```bash
   # Node.js, npm, git
   ```
3. Install OpenClaw:
   ```bash
   npm install -g openclaw
   ```
4. Clone workspace from GitHub
5. Restore configuration from encrypted backup
6. Configure channels (Telegram, email)
7. Test full functionality

## Verification & Testing

### Quarterly Recovery Test
1. **Test Date:** First week of each quarter
2. **Process:**
   - Simulate workspace loss
   - Execute recovery steps
   - Measure recovery time
   - Document any issues
3. **Success Criteria:** Full functionality restored within 2 hours

### Monthly Backup Verification
1. Check GitHub commit history
2. Verify configuration backups exist
3. Test email/SMTP functionality
4. Verify cron jobs are active

## Security Considerations

### Sensitive Data
- **Never commit:** API keys, passwords, auth tokens
- **Encrypt:** Configuration files containing credentials
- **Store securely:** Use OpenClaw secret management when available

### Access Control
- **GitHub:** Private repository required
- **Backup location:** Encrypted external storage
- **Recovery credentials:** Store separately from backups

## Automation Status

### ✅ Currently Automated
- Workspace git backup (every 6 hours)
- Pre-change backups (via `pre-change-backup.sh`)

### 🔄 Planned Automation
- Configuration backup automation
- Backup verification alerts
- Recovery script generation

## Contact & Escalation

### Primary
- **Marrs Coiro:** marrs@polynize.io
- **Richie:** Telegram notification

### Secondary
- **Shourov:** Technical co-founder
- **Kenny:** Infrastructure lead

## Version History
- **2026-03-13:** Initial protocol created by Darren
- **Next Review:** 2026-06-13