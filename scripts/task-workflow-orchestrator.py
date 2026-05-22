#!/usr/bin/env python3
"""
Task Workflow Orchestrator - PACED & SILENT
Complete workflow: approved → doing → execution → done

SILENT MODE (default for cron):
- Set SILENT=1 environment variable
- NO output unless human attention required
- Logs to ~/.openclaw/logs/paced-workflow.log
"""

import subprocess
import sys
import os
from datetime import datetime

LOG_FILE = os.path.expanduser("~/.openclaw/logs/paced-workflow.log")

def log(message):
    """Log to file only (silent)"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, 'a') as f:
            f.write(log_line + '\n')
    except:
        pass
    # Note: This function NEVER prints to stdout - always silent

def run_script(script_name):
    """Run a Python script silently"""
    script_path = f"/Users/openclaw_admin/.openclaw/workspace/scripts/{script_name}"
    
    if not os.path.exists(script_path):
        log(f"Error: Script not found: {script_path}")
        return None
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(script_path)
        )
        
        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "returncode": 1
        }

def main():
    """Orchestrate the complete task workflow - SILENTLY"""
    
    log("=== WORKFLOW START ===")
    
    attention_needed = []
    spawned_agents = []
    
    # Step 1: Process approved tasks (todo → doing)
    log("Step 1: Processing approved tasks (todo → doing)")
    approval_result = run_script("approved-task-executor-limited.py")
    
    if approval_result["success"]:
        log("Step 1: Success - approved task moved to doing")
    else:
        log(f"Step 1: No approved tasks or error")
    
    # Step 2: Execute tasks in doing status
    log("Step 2: Executing tasks (doing → agent spawn)")
    execution_result = run_script("agent-task-spawner-limited.py")
    
    if execution_result["success"]:
        output = execution_result.get("output", "")
        log("Step 2: Success - agent spawned or no tasks")
        
        # Check if agent was spawned
        if "spawned successfully" in output.lower():
            # Extract task name if possible
            spawned_agents.append("Agent task executed")
    else:
        log(f"Step 2: No tasks to execute or error")
    
    log("=== WORKFLOW COMPLETE ===")
    
    # SILENT MODE: Only output if human attention needed
    if attention_needed:
        print("⚠️ TASKS NEED ATTENTION:")
        for item in attention_needed:
            print(f"  • {item}")
    # Otherwise: COMPLETE SILENCE - no output at all

if __name__ == "__main__":
    main()
