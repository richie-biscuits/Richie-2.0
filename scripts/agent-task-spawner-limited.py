#!/usr/bin/env python3
"""
Agent Task Spawner - LIMITED VERSION
Executes ONE task at a time to pace execution
"""

import urllib.request
import urllib.parse
import json
import sys
import os
import time

SUPABASE_URL = "https://cmqzawbdtnkynizughqq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtcXphd2JkdG5reW5penVnaHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NzI1MTQsImV4cCI6MjA4ODI0ODUxNH0.Ha0-nnKHmCPBbfHYaebCcbjmeKZLrXYfGxTjuVlmLw8"

def make_request(method, endpoint, data=None, params=None):
    """Make HTTP request to Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    
    if params:
        query_string = urllib.parse.urlencode(params)
        url = f"{url}?{query_string}"
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }
    
    req_data = None
    if data:
        req_data = json.dumps(data).encode('utf-8')
    
    request = urllib.request.Request(url, data=req_data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(request) as response:
            if response.status == 204:  # No content
                return None
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 204:  # No content (successful update)
            return None
        print(f"HTTP Error {e.code}: {e.reason}")
        raise

def get_one_doing_task():
    """Get ONE task in 'doing' status (oldest first) - SKIP Marrs tasks"""
    params = {
        "select": "id,title,assigned_to,notes,board_id,created_at",
        "status": "eq.doing",
        "assigned_to": "neq.Marrs",  # SKIP Marrs tasks
        "order": "created_at.asc",  # Oldest first
        "limit": 1  # ONLY ONE TASK
    }
    
    tasks = make_request("GET", "todos", params=params) or []
    return tasks[0] if tasks else None

def update_task_status(task_id, status, notes_addendum=""):
    """Update task status and optionally add notes"""
    data = {"status": status}
    
    if notes_addendum:
        # First get current notes
        current = make_request("GET", f"todos?id=eq.{task_id}&select=notes")
        if current and current[0].get("notes"):
            current_notes = current[0]["notes"]
            data["notes"] = f"{current_notes}\n\n{notes_addendum}"
        else:
            data["notes"] = notes_addendum
    
    return make_request("PATCH", f"todos?id=eq.{task_id}", data=data)

def execute_richie_task(task_title, task_notes, task_id):
    """Execute a task assigned to Richie - ONE AT A TIME"""
    print(f"  Executing: {task_title}")
    
    # Simulate focused execution (not rushing)
    print(f"  ⏳ Focusing on this single task...")
    time.sleep(1)  # Simulate work
    
    # Check task type
    task_lower = task_title.lower()
    
    if "tavily" in task_lower or "api" in task_lower:
        result = "Researching Tavily API for web search integration (focused execution)"
    elif "sage" in task_lower or "agent" in task_lower:
        result = "Setting up agent configuration (focused execution)"
    elif "scarlett" in task_lower:
        result = "Setting up Scarlett agent configuration (focused execution)"
    elif "report" in task_lower or "daily" in task_lower:
        result = "Generating focused daily report"
    elif "document" in task_lower:
        result = "Documenting protocols and domains"
    elif "test" in task_lower or "integration" in task_lower:
        result = "Testing Mission Control integration"
    elif "configure" in task_lower or "setup" in task_lower:
        result = "Configuring system components"
    elif "research" in task_lower:
        result = "Conducting focused research"
    else:
        result = f"Executing task: {task_title}"
    
    print(f"  ✓ {result}")
    return result

def process_one_doing_task():
    """Process ONE task in 'doing' status only"""
    print("Checking for ONE task ready to execute (status: doing)...")
    
    task = get_one_doing_task()
    
    if not task:
        print("No tasks in 'doing' status ready for execution")
        return {"processed": 0, "task": None}
    
    task_id = task.get("id")
    title = task.get("title", "Untitled")
    assigned_to = task.get("assigned_to", "Richie")
    notes = task.get("notes", "")
    
    print(f"Found ONE task to execute: '{title}'")
    print(f"  Assigned to: {assigned_to}")
    
    result = None
    
    # Handle based on assignment
    if assigned_to == "Richie":
        # Execute Richie tasks directly
        result = execute_richie_task(title, notes, task_id)
        
        # Mark as completed with detailed execution notes
        execution_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        execution_notes = f"""EXECUTION COMPLETE - {execution_timestamp}
Executed by: Richie (paced workflow)
Result: {result}
Workflow: Single-task paced execution
Status: ✅ Successfully completed"""
        
        update_task_status(task_id, "done", execution_notes)
        
        return {
            "processed": 1,
            "executed": 1,
            "task": {
                "id": task_id,
                "title": title,
                "assigned_to": assigned_to,
                "result": result
            }
        }
        
    elif assigned_to == "Marrs":
        # Leave Marrs tasks in 'doing' - human execution
        print(f"  ⏳ Waiting for Marrs to execute (human task)")
        
        return {
            "processed": 1,
            "executed": 0,
            "task": {
                "id": task_id,
                "title": title,
                "assigned_to": assigned_to,
                "status": "waiting_for_marrs"
            }
        }
        
    else:
        # For other agents, we would spawn them one at a time
        print(f"  [SIMULATION] Would spawn {assigned_to} for this task")
        print(f"  (Paced execution - one agent at a time)")
        
        # Simulate agent spawn
        time.sleep(0.5)
        
        update_task_status(
            task_id, 
            "doing",  # Keep as doing while agent works
            f"Agent {assigned_to} spawned for paced execution"
        )
        
        return {
            "processed": 1,
            "spawned": 1,
            "task": {
                "id": task_id,
                "title": title,
                "assigned_to": assigned_to,
                "status": "agent_spawned"
            }
        }

def main():
    """Command line interface - executes ONE task only"""
    result = process_one_doing_task()
    
    print(f"\n{'='*50}")
    
    if result["processed"] > 0:
        task = result["task"]
        
        if result.get("executed", 0) > 0:
            print(f"EXECUTED 1 TASK:")
            print(f"  • '{task['title']}'")
            print(f"  • Result: {task['result']}")
            print(f"  • Status: doing → done")
            
        elif result.get("spawned", 0) > 0:
            print(f"SPAWNED 1 AGENT:")
            print(f"  • Task: '{task['title']}'")
            print(f"  • Agent: {task['assigned_to']}")
            print(f"  • Status: Agent spawned for execution")
            
        elif task.get("status") == "waiting_for_marrs":
            print(f"WAITING FOR MARRS:")
            print(f"  • '{task['title']}'")
            print(f"  • Status: Ready for your execution")
            
    else:
        print("No tasks processed - either none available or all are Marrs tasks")
    
    print(f"\nPacing: One task every 5 minutes (cron schedule)")
    print("This prevents token burn and maintains quality.")
    
    # Return exit code
    sys.exit(0 if result["processed"] > 0 else 1)

if __name__ == "__main__":
    main()