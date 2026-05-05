#!/usr/bin/env python3
"""
Task Workflow Orchestrator
Complete workflow: approved → doing → execution → done
Combines both approval processing and agent spawning

SILENT MODE: Set SILENT=1 environment variable for cron operation
"""

import subprocess
import sys
import os
from datetime import datetime

# Check for silent mode
SILENT = os.environ.get('SILENT', '0') == '1' or os.environ.get('SILENT_MODE', '0') == '1'
LOG_FILE = os.path.expanduser("~/.openclaw/logs/paced-workflow.log")

def log(message):
    """Log to file and optionally print"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}"
    
    # Always write to log file
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, 'a') as f:
            f.write(log_line + '\n')
    except:
        pass
    
    # Only print if not in silent mode
    if not SILENT:
        print(message)

def run_script(script_name):
    """Run a Python script and capture output"""
    script_path = f"/Users/openclaw_admin/.openclaw/workspace/scripts/{script_name}"
    
    if not os.path.exists(script_path):
        log(f"Error: Script not found: {script_path}")
        return None
    
    try:
        # Pass silent mode to child scripts
        env = os.environ.copy()
        env['SILENT'] = '1' if SILENT else '0'
        
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(script_path),
            env=env
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
    """Orchestrate the complete task workflow"""
    
    if not SILENT:
        print("=" * 60)
        print("TASK WORKFLOW ORCHESTRATOR")
        print("=" * 60)
    
    log("Workflow started")
    
    # Track if anything needs human attention
    needs_attention = []
    tasks_completed = []
    
    # Step 1: Process approved tasks (todo → doing)
    if not SILENT:
        print("\n1. PROCESSING APPROVED TASKS (todo → doing)")
        print("-" * 40)
    
    approval_result = run_script("approved-task-executor-limited.py")
    
    if approval_result["success"]:
        output = approval_result["output"]
        if not SILENT:
            print(output)
        
        # Check for tasks that were moved
        if "Moved 1 task" in output:
            # Extract task name
            for line in output.split('\n'):
                if "→ 'doing':" in line:
                    task_name = line.split("→ 'doing':")[-1].strip()
                    log(f"Approved task moved to doing: {task_name}")
                    break
    else:
        log(f"Failed to process approved tasks: {approval_result.get('error', 'Unknown error')}")
    
    # Step 2: Execute tasks in doing status
    if not SILENT:
        print("\n2. EXECUTING TASKS (doing → execution)")
        print("-" * 40)
    
    execution_result = run_script("agent-task-spawner-limited.py")
    
    if execution_result["success"]:
        output = execution_result["output"]
        if not SILENT:
            print(output)
        
        # Check for completed tasks requiring attention
        if "COMPLETED - Needs Review" in output:
            for line in output.split('\n'):
                if "COMPLETED - Needs Review" in line:
                    needs_attention.append(line.strip())
        
        # Check for tasks completed by Marrs (stay in doing)
        if "Tasks completed by Richie:" in output:
            for line in output.split('\n'):
                if line.strip().startswith("-"):
                    tasks_completed.append(line.strip())
    else:
        log(f"Failed to execute tasks: {execution_result.get('error', 'Unknown error')}")
    
    log("Workflow completed")
    
    # In silent mode, only output if something needs human attention
    if SILENT:
        if needs_attention:
            print("⚠️ TASKS COMPLETED - NEED REVIEW:")
            for task in needs_attention:
                print(f"  {task}")
            return 0
        elif tasks_completed:
            # Tasks completed but no review needed - truly silent
            return 0
        else:
            # Nothing happened - truly silent
            return 0
    
    # Non-silent mode - show full summary
    print("\n" + "=" * 60)
    print("WORKFLOW COMPLETE")
    print("=" * 60)
    
    if needs_attention:
        print("\n⚠️ TASKS NEEDING REVIEW:")
        for task in needs_attention:
            print(f"  • {task}")
    
    print("\nNEXT STEPS:")
    print("1. Check Mission Control for updated task statuses")
    print("2. Review completed tasks in 'done' column")
    print("3. Approve more tasks as needed")
    print("4. Tasks assigned to Marrs remain in 'doing' for manual execution")
    
    print("\nQUICK COMMANDS:")
    print("  • Check pending: python3 mission_approve_simple.py pending")
    print("  • Run workflow: python3 scripts/task-workflow-orchestrator.py")
    print("  • Manual approve: python3 mission_approve_simple.py toggle <task_id>")

if __name__ == "__main__":
    main()
