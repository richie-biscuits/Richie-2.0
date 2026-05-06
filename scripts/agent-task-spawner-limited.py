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
import subprocess

SUPABASE_URL = "https://cmqzawbdtnkynizughqq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtcXphd2JkdG5reW5penVnaHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NzI1MTQsImV4cCI6MjA4ODI0ODUxNH0.Ha0-nnKHmCPBbfHYaebCcbjmeKZLrXYfGxTjuVlmLw8"

SILENT = os.environ.get('SILENT', '0') == '1'

def log(msg):
    if not SILENT:
        print(msg)

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
            if response.status == 204:
                return None
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 204:
            return None
        log(f"HTTP Error {e.code}: {e.reason}")
        raise

def get_one_doing_task():
    """Get ONE task in 'doing' status (oldest first) - SKIP Marrs tasks"""
    params = {
        "select": "id,title,assigned_to,notes,board_id,created_at",
        "status": "eq.doing",
        "assigned_to": "neq.Marrs",
        "order": "created_at.asc",
        "limit": 1
    }
    
    tasks = make_request("GET", "todos", params=params) or []
    return tasks[0] if tasks else None

def update_task_status(task_id, status, notes_addendum=""):
    """Update task status and optionally add notes"""
    data = {"status": status}
    
    if notes_addendum:
        current = make_request("GET", f"todos?id=eq.{task_id}&select=notes")
        if current and current[0].get("notes"):
            current_notes = current[0]["notes"]
            data["notes"] = f"{current_notes}\n\n{notes_addendum}"
        else:
            data["notes"] = notes_addendum
    
    return make_request("PATCH", f"todos?id=eq.{task_id}", data=data)

def spawn_agent_for_task(agent_id, task_title, task_notes):
    """Actually spawn an agent using openclaw sessions spawn"""
    if not agent_id:
        log("  ✗ No agent assigned to task")
        return False
    
    # Prepare the task description
    task_description = f"""Task from Mission Control:
Title: {task_title}
Notes: {task_notes[:2000] if task_notes else 'No additional notes'}

Please complete this task and report back when done."""
    
    try:
        cmd = [
            "openclaw", "sessions", "spawn",
            "--agent-id", agent_id.lower(),
            "--task", task_description,
            "--mode", "run"
        ]
        
        log(f"  🚀 Spawning agent: {agent_id}")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            log(f"  ✓ Agent {agent_id} spawned successfully")
            return True
        else:
            log(f"  ✗ Failed to spawn agent: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        log(f"  ✗ Agent spawn timed out")
        return False
    except Exception as e:
        log(f"  ✗ Error spawning agent: {e}")
        return False

def process_one_doing_task():
    """Process ONE task in 'doing' status only"""
    log("Checking for ONE task ready to execute (status: doing)...")
    
    task = get_one_doing_task()
    
    if not task:
        log("No tasks in 'doing' status ready for execution")
        return {"processed": 0, "task": None}
    
    task_id = task.get("id")
    title = task.get("title", "Untitled")
    assigned_to = task.get("assigned_to", "")
    notes = task.get("notes", "")
    
    log(f"Found ONE task to execute: '{title}'")
    log(f"  Assigned to: {assigned_to or 'Unassigned'}")
    
    # Skip if no agent assigned
    if not assigned_to:
        log("  ⚠️ Task has no assigned agent - skipping")
        return {"processed": 0, "task": None, "error": "no_agent"}
    
    # Handle based on assignment
    if assigned_to == "Richie":
        # Richie tasks should be handled by the main assistant
        log(f"  ⏳ Richie task - main assistant will handle")
        return {
            "processed": 1,
            "executed": 0,
            "richie": True,
            "task": {
                "id": task_id,
                "title": title,
                "assigned_to": assigned_to
            }
        }
        
    elif assigned_to == "Marrs":
        # Should not happen due to query filter, but handle anyway
        log(f"  ⏳ Waiting for Marrs to execute (human task)")
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
        # Spawn the actual agent
        spawn_success = spawn_agent_for_task(assigned_to, title, notes)
        
        if spawn_success:
            # Move to 'done' since agent is now handling it
            execution_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            execution_notes = f"""AGENT SPAWNED - {execution_timestamp}
Agent: {assigned_to}
Status: Agent spawned and executing task
Workflow: Paced execution (one at a time)"""
            
            update_task_status(task_id, "done", execution_notes)
            
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
        else:
            # Spawn failed - keep in doing for retry
            return {
                "processed": 1,
                "spawned": 0,
                "error": "spawn_failed",
                "task": {
                    "id": task_id,
                    "title": title,
                    "assigned_to": assigned_to
                }
            }

def main():
    result = process_one_doing_task()
    
    if not SILENT:
        print(f"\n{'='*50}")
        
        if result["processed"] > 0:
            task = result["task"]
            
            if result.get("richie"):
                print(f"RICHIE TASK:")
                print(f"  • '{task['title']}'")
                print(f"  • Main assistant will handle")
                
            elif result.get("spawned", 0) > 0:
                print(f"SPAWNED 1 AGENT:")
                print(f"  • Task: '{task['title']}'")
                print(f"  • Agent: {task['assigned_to']}")
                print(f"  • Status: Agent spawned → done")
                
            elif result.get("error") == "spawn_failed":
                print(f"SPAWN FAILED:")
                print(f"  • '{task['title']}'")
                print(f"  • Agent: {task['assigned_to']}")
                print(f"  • Will retry on next run")
                
            elif task.get("status") == "waiting_for_marrs":
                print(f"WAITING FOR MARRS:")
                print(f"  • '{task['title']}'")
                print(f"  • Status: Ready for your execution")
                
        else:
            if result.get("error") == "no_agent":
                print("Skipped: Task has no assigned agent")
            else:
                print("No tasks processed - none available")
        
        print(f"\nPacing: One task every 30 minutes (cron schedule)")
    
    sys.exit(0 if result.get("spawned") or result.get("richie") else 1)

if __name__ == "__main__":
    main()
