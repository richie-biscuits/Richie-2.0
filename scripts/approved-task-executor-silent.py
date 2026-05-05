#!/usr/bin/env python3
"""
Approved Task Executor - SILENT VERSION
Processes only ONE approved task at a time - completely silent
"""

import urllib.request
import urllib.parse
import json
import sys
import os
from datetime import datetime

SUPABASE_URL = "https://cmqzawbdtnkynizughqq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNtcXphd2JkdG5reW5penVnaHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI2NzI1MTQsImV4cCI6MjA4ODI0ODUxNH0.Ha0-nnKHmCPBbfHYaebCcbjmeKZLrXYfGxTjuVlmLw8"

LOG_FILE = os.path.expanduser("~/.openclaw/logs/paced-workflow.log")

def log(message):
    """Log to file only (silent)"""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] [APPROVAL] {message}\n")

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

def get_one_approved_todo_task():
    """Get ONE approved task in todo status (oldest first)"""
    params = {
        "select": "id,title,assigned_to,notes,board_id,created_at",
        "status": "eq.todo",
        "approved": "eq.true",
        "order": "created_at.asc",
        "limit": 1
    }
    
    tasks = make_request("GET", "todos", params=params) or []
    return tasks[0] if tasks else None

def update_task_status(task_id, status):
    """Update task status (todo → doing → done)"""
    data = {"status": status}
    return make_request("PATCH", f"todos?id=eq.{task_id}", data=data)

def process_one_approved_task():
    """Process ONE approved task only - SILENTLY"""
    task = get_one_approved_todo_task()
    
    if not task:
        # No tasks - silent, just log
        log("No approved tasks waiting in todo status")
        return {"processed": 0, "task": None}
    
    task_id = task.get("id")
    title = task.get("title", "Untitled")
    assigned_to = task.get("assigned_to", "Richie")
    
    log(f"Processing task: '{title}' (assigned to: {assigned_to})")
    
    # Update status from todo → doing
    try:
        update_task_status(task_id, "doing")
        log(f"Successfully moved to 'doing' status")
        
        return {
            "processed": 1,
            "task": {
                "id": task_id,
                "title": title,
                "assigned_to": assigned_to,
                "notes": task.get("notes", "")
            }
        }
    except Exception as e:
        log(f"Failed to update status: {e}")
        return {"processed": 0, "task": None, "error": str(e)}

def main():
    """Command line interface - processes ONE task only - SILENT"""
    result = process_one_approved_task()
    
    if result["processed"] > 0:
        task = result["task"]
        log(f"PROCESSED 1 TASK: '{task['title']}' assigned to {task['assigned_to']}")
        # Print minimal output for orchestrator to detect
        print(f"PROCESSED 1 TASK: todo → doing")
        sys.exit(0)
    else:
        log("No tasks processed")
        # Silent - no output
        sys.exit(1)

if __name__ == "__main__":
    main()
