#!/usr/bin/env python3
"""
Task Workflow Orchestrator
Complete workflow: approved → doing → execution → done
Combines both approval processing and agent spawning
"""

import subprocess
import sys
import os

def run_script(script_name):
    """Run a Python script and capture output"""
    script_path = f"/Users/openclaw_admin/.openclaw/workspace/scripts/{script_name}"
    
    if not os.path.exists(script_path):
        print(f"Error: Script not found: {script_path}")
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
    """Orchestrate the complete task workflow"""
    print("=" * 60)
    print("TASK WORKFLOW ORCHESTRATOR")
    print("=" * 60)
    
    # Step 1: Process approved tasks (todo → doing)
    print("\n1. PROCESSING APPROVED TASKS (todo → doing)")
    print("-" * 40)
    
    approval_result = run_script("approved-task-executor-limited.py")
    
    if approval_result["success"]:
        print(approval_result["output"])
        
        # Extract number of processed tasks from output
        output = approval_result["output"]
        if "Processed" in output:
            # Find the line with "Processed X task(s)"
            for line in output.split('\n'):
                if "Processed" in line and "task" in line:
                    print(f"\n✓ {line.strip()}")
                    break
    else:
        print(f"✗ Failed to process approved tasks: {approval_result.get('error', 'Unknown error')}")
    
    # Step 2: Execute tasks in doing status
    print("\n2. EXECUTING TASKS (doing → execution)")
    print("-" * 40)
    
    execution_result = run_script("agent-task-spawner-limited.py")
    
    if execution_result["success"]:
        print(execution_result["output"])
        
        # Check if any tasks were executed
        output = execution_result["output"]
        if "Tasks completed by Richie:" in output:
            print("\n✓ Tasks executed successfully")
        elif "No tasks in 'doing' status" in output:
            print("\nℹ️ No tasks ready for execution")
    else:
        print(f"✗ Failed to execute tasks: {execution_result.get('error', 'Unknown error')}")
    
    # Step 3: Summary
    print("\n" + "=" * 60)
    print("WORKFLOW COMPLETE")
    print("=" * 60)
    
    # Provide actionable summary
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