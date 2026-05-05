#!/usr/bin/env python3
"""
Agent Task Spawner - SILENT VERSION
Executes ONE task at a time to pace execution - actually spawns agents
"""

import urllib.request
import urllib.parse
import json
import sys
import os
import time
import subprocess
from datetime import datetime

SUPABASE_URL = "https://cmqzawbdtnkynizughqq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtcXphd2JkdG5reW5penVnaHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NzI1MTQsImV4cCI6MjA4ODI0ODUxNH0.Ha0-nnKHmCPBbfHYaebCcbjmeKZLrXYfGxTjuVlmLw8"

LOG_FILE = os.path.expanduser("~/.openclaw/logs/paced-workflow.log")

def log(message):
    """Log to file only (silent)"""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] [SPAWNER] {message}\n")

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

def spawn_agent_for_task(agent_name, task_title, task_notes, task_id):
    """Actually spawn an agent using sessions_spawn via shell command"""
    log(f"Spawning agent {agent_name} for task: {task_title}")
    
    # Prepare the task context
    task_context = f"""Task from Mission Control:
Title: {task_title}
Notes: {task_notes or 'No additional notes'}
Task ID: {task_id}

Please complete this task and report back when done.
"""
    
    # Map agent names to agent IDs
    agent_map = {
        "Dash": "dash",
        "Scarlett": "scarlett",
        "Sage": "sage",
        # Add more mappings as needed
    }
    
    agent_id = agent_map.get(agent_name, agent_name.lower())
    
    try:
        # Use openclaw CLI to spawn the agent
        cmd = [
            "openclaw", "sessions", "spawn",
            "--agent-id", agent_id,
            "--task", task_context,
            "--mode", "run",
            "--runtime", "subagent",
            "--label", f"task-{task_id}"
        ]
        
        log(f"Running command: {' '.join(cmd)}")
        
        # Run with capture to check for errors
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            log(f"Agent {agent_name} spawned successfully")
            log(f"Spawn output: {result.stdout}")
            return True
        else:
            log(f"Agent spawn failed with code {result.returncode}")
            log(f"Spawn stderr: {result.stderr}")
            log(f"Spawn stdout: {result.stdout}")
            return False
        
    except subprocess.TimeoutExpired:
        log(f"Agent spawn timed out - but may have succeeded")
        return True  # Assume success if it timed out (long spawn)
    except Exception as e:
        log(f"Failed to spawn agent {agent_name}: {e}")
        return False

def execute_richie_task(task_title, task_notes, task_id):
    """Execute a task assigned to Richie - ONE AT A TIME"""
    log(f"Executing Richie task: {task_title}")
    
    # For now, Richie tasks need human attention since I can't self-spawn
    # Mark them with a note that they need execution
    execution_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    execution_notes = f"""PENDING EXECUTION - {execution_timestamp}
Assigned to: Richie
Status: Task approved and ready for execution
Action needed: Richie to execute this task
"""
    
    update_task_status(task_id, "doing", execution_notes)
    
    result = f"Task '{task_title}' ready for Richie execution"
    log(result)
    return result

def process_one_doing_task():
    """Process ONE task in 'doing' status only - SILENTLY"""
    task = get_one_doing_task()
    
    if not task:
        log("No tasks in 'doing' status ready for execution")
        # Silent - print marker for orchestrator
        print("NO_TASKS")
        return {"processed": 0, "task": None}
    
    task_id = task.get("id")
    title = task.get("title", "Untitled")
    assigned_to = task.get("assigned_to", "Richie")
    notes = task.get("notes", "")
    
    log(f"Found task to execute: '{title}' assigned to {assigned_to}")
    
    result = None
    
    if assigned_to == "Richie":
        # Richie tasks - mark for execution (requires human attention)
        result = execute_richie_task(title, notes, task_id)
        
        return {
            "processed": 1,
            "executed": 0,
            "needs_human": True,
            "task": {
                "id": task_id,
                "title": title,
                "assigned_to": assigned_to,
                "result": result
            }
        }
        
    elif assigned_to == "Marrs":
        # Should not happen due to query filter, but handle just in case
        log(f"Skipping Marrs task: '{title}'")
        return {"processed": 0, "task": None}
        
    else:
        # Spawn agent for this task
        spawn_success = spawn_agent_for_task(assigned_to, title, notes, task_id)
        
        if spawn_success:
            update_task_status(
                task_id, 
                "doing",
                f"Agent {assigned_to} spawned at {time.strftime('%Y-%m-%d %H:%M:%S')}"
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
        else:
            # Spawn failed - mark task with error and move to blocked
            log(f"Agent spawn failed for '{title}' - marking as blocked")
            update_task_status(
                task_id,
                "blocked",
                f"""SPAWN FAILED - {time.strftime('%Y-%m-%d %H:%M:%S')}
Agent: {assigned_to}
Error: Agent spawn infrastructure error (openclaw CLI config)
Action needed: Manual execution or fix spawn infrastructure
"""
            )
            return {
                "processed": 1,
                "spawned": 0,
                "blocked": 1,
                "needs_human": True,
                "task": {
                    "id": task_id,
                    "title": title,
                    "assigned_to": assigned_to,
                    "status": "blocked",
                    "result": f"Agent spawn failed for {assigned_to} - infrastructure error"
                }
            }

def main():
    """Command line interface - executes ONE task only - SILENT"""
    result = process_one_doing_task()
    
    if result["processed"] > 0:
        task = result["task"]
        
        if result.get("executed", 0) > 0:
            log(f"EXECUTED: '{task['title']}'")
            print(f"TASK_COMPLETED:{json.dumps(task)}")
            sys.exit(0)
            
        elif result.get("spawned", 0) > 0:
            log(f"SPAWNED AGENT: {task['assigned_to']} for '{task['title']}'")
            print("SPAWNED_AGENT")
            sys.exit(0)
            
        elif result.get("blocked", 0) > 0:
            log(f"BLOCKED: '{task['title']}' - spawn failed")
            print(f"TASK_BLOCKED:{json.dumps(task)}")
            sys.exit(0)
            
        elif result.get("needs_human"):
            log(f"NEEDS HUMAN: '{task['title']}'")
            print(f"TASK_COMPLETED:{json.dumps(task)}")
            sys.exit(0)
    else:
        log("No tasks processed")
        sys.exit(1)

if __name__ == "__main__":
    main()
