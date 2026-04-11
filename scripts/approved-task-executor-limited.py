#!/usr/bin/env python3
"""
Approved Task Executor - LIMITED VERSION
Processes only ONE approved task at a time to pace execution
"""

import urllib.request
import urllib.parse
import json
import sys
import os

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

def get_one_approved_todo_task():
    """Get ONE approved task in todo status (oldest first)"""
    params = {
        "select": "id,title,assigned_to,notes,board_id,created_at",
        "status": "eq.todo",
        "approved": "eq.true",
        "order": "created_at.asc",  # Oldest first
        "limit": 1  # ONLY ONE TASK
    }
    
    tasks = make_request("GET", "todos", params=params) or []
    return tasks[0] if tasks else None

def update_task_status(task_id, status):
    """Update task status (todo → doing → done)"""
    data = {"status": status}
    return make_request("PATCH", f"todos?id=eq.{task_id}", data=data)

def process_one_approved_task():
    """Process ONE approved task only"""
    print("Checking for ONE approved task to process...")
    
    task = get_one_approved_todo_task()
    
    if not task:
        print("No approved tasks waiting in todo status")
        return {"processed": 0, "task": None}
    
    task_id = task.get("id")
    title = task.get("title", "Untitled")
    assigned_to = task.get("assigned_to", "Richie")
    
    print(f"Found ONE task to process: '{title}' (assigned to: {assigned_to})")
    
    # Update status from todo → doing
    try:
        update_task_status(task_id, "doing")
        print(f"✓ Moved to 'doing' status")
        
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
        print(f"✗ Failed to update status: {e}")
        return {"processed": 0, "task": None, "error": str(e)}

def main():
    """Command line interface - processes ONE task only"""
    result = process_one_approved_task()
    
    print(f"\n{'='*50}")
    
    if result["processed"] > 0:
        task = result["task"]
        print(f"PROCESSED 1 TASK:")
        print(f"  • '{task['title']}'")
        print(f"  • Assigned to: {task['assigned_to']}")
        print(f"  • Status: todo → doing")
        print(f"\nNext: This task will be executed in the next step.")
    else:
        print("No tasks processed - either none available or error occurred")
    
    # Return exit code
    sys.exit(0 if result["processed"] > 0 else 1)

if __name__ == "__main__":
    main()