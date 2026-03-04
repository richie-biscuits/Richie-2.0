# Chronicles — Richie & Marrs

A chronological record of our work together. Simple, factual, searchable.

---

## 2026-02-27 — Hutcho Sentinel First Run
- **Security baseline established**
- Deployed Hutcho Sentinel security agent
- First assessment: Band 4 STRONG / Score 95 / PASS
- Noted: Sandbox mode OFF (acceptable for current trust level)

---

## 2026-03-04 — Model Routing & Backup Systems

### Morning/Afternoon (before 4:19 PM)
- Created model routing configuration in TOOLS.md
- Defined auto-router logic (Kimi → Sonnet → Opus based on task type)
- Documented cost awareness and fallback chains

### 4:19 PM — Auto-Backup
- Workspace auto-backed up with TOOLS.md changes

### Evening (6:18 PM onwards)
- Restored workspace to 4:19 PM backup after session reset
- Set up automatic GitHub backups every 6 hours via cron
- Created `pre-change-backup.sh` script for safety
- Added mandatory pre-change backup rule to AGENTS.md
- Created this Chronicles.md file

---

*Format: Date — What we did. Keep it simple.*
