#!/usr/bin/env python3
"""
Task Workflow Orchestrator - SILENT VERSION
Completely silent execution - only outputs if human attention needed
Logs all activity to file
"""

import subprocess
import sys
import os
import json
from datetime import datetime

LOG_FILE = os.path.expanduser("~/.openclaw/logs/paced-workflow.log")

def log(message):
    """Log to file only (silent)"""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def run_script_silent(script_name):
    """Run a Python script silently, capture all output"""
    script_path = f"/Users/openclaw_admin/.openclaw/workspace/scripts/{script_name}"
    
    if not os.path.exists(script_path):
        log(f"ERROR: Script not found: {script_path}")
        return None
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(script_path)
        )
        
        # Log all output to file (silent)
        if result.stdout:
            log(f"STDOUT from {script_name}:\n{result.stdout}")
        if result.stderr:
            log(f"STDERR from {script_name}:\n{result.stderr}")
        
        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        log(f"EXCEPTION running {script_name}: {e}")
        return {
            "success": False,
            "error": str(e),
            "returncode": 1
        }

def main():
    """Orchestrate the complete task workflow - SILENTLY"""
    log("=" * 60)
    log("TASK WORKFLOW ORCHESTRATOR (SILENT MODE)")
    log("=" * 60)
    
    human_attention_needed = []
    blocked_tasks = []
    
    # Step 1: Process approved tasks (todo → doing)
    log("Step 1: Processing approved tasks (todo → doing)")
    approval_result = run_script_silent("approved-task-executor-silent.py")
    
    if not approval_result or not approval_result["success"]:
        error = approval_result.get("error", "Unknown error") if approval_result else "No result"
        log(f"Step 1 FAILED: {error}")
        # Don't output - keep silent unless it's a critical error
    else:
        output = approval_result.get("output", "")
        if "PROCESSED 1 TASK" in output:
            log("Step 1 SUCCESS: Processed 1 approved task")
        else:
            log("Step 1: No approved tasks to process")
    
    # Step 2: Execute tasks in doing status
    log("Step 2: Executing tasks (doing → execution)")
    execution_result = run_script_silent("agent-task-spawner-silent.py")
    
    if not execution_result or not execution_result["success"]:
        error = execution_result.get("error", "Unknown error") if execution_result else "No result"
        log(f"Step 2 FAILED: {error}")
    else:
        output = execution_result.get("output", "")
        
        # Check for completed tasks requiring human attention
        if "TASK_COMPLETED" in output:
            # Extract task info from output
            for line in output.split("\n"):
                if line.startswith("TASK_COMPLETED:"):
                    try:
                        task_data = json.loads(line.replace("TASK_COMPLETED:", ""))
                        human_attention_needed.append(task_data)
                        log(f"Task completed requiring attention: {task_data}")
                    except:
                        pass
        
        # Check for blocked tasks
        if "TASK_BLOCKED" in output:
            for line in output.split("\n"):
                if line.startswith("TASK_BLOCKED:"):
                    try:
                        task_data = json.loads(line.replace("TASK_BLOCKED:", ""))
                        blocked_tasks.append(task_data)
                        log(f"Task blocked: {task_data}")
                    except:
                        pass
        
        if "SPAWNED_AGENT" in output:
            log("Agent spawned successfully")
        
        if "NO_TASKS" in output:
            log("No tasks in doing status")
    
    log("=" * 60)
    log("WORKFLOW COMPLETE")
    log("=" * 60)
    
    # ONLY OUTPUT IF HUMAN ATTENTION NEEDED
    output_needed = False
    
    if blocked_tasks:
        print(f"\n⚠️  {len(blocked_tasks)} task(s) BLOCKED - agent spawn failed:")
        for task in blocked_tasks:
            print(f"  • '{task.get('title', 'Untitled')}'")
            print(f"    Assigned to: {task.get('assigned_to', 'Unknown')}")
            print(f"    Issue: {task.get('result', 'Infrastructure error')}")
            print(f"    Action: Check Mission Control or fix openclaw CLI config")
        print()
        output_needed = True
    
    if human_attention_needed:
        print(f"\n🎯 {len(human_attention_needed)} task(s) completed and require your review:")
        for task in human_attention_needed:
            print(f"  • '{task.get('title', 'Untitled')}'")
            print(f"    Result: {task.get('result', 'N/A')[:100]}...")
            print(f"    Status: Completed → Review in Mission Control")
        print()
        output_needed = True
    
    if not output_needed:
        # COMPLETE SILENCE - no output
        log("No human attention needed - remaining silent")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
