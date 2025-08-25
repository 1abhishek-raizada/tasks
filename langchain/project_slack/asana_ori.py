import os
import re
import html
from dotenv import load_dotenv
from asana import Client as AsanaClient
from datetime import datetime, timedelta, timezone
 
# Your Asana Project GID
project_gid = '1209119248553524'
 
# Your Asana Personal Access Token (PAT)
ASANA_TOKEN = "2/1210688947914366/1210689712265877:a5e68803c483482562b3fc06491fabf7"
 
# Initialize Asana client
asana_client = AsanaClient.access_token(ASANA_TOKEN)
 
def get_task_completion_from_status_links(project_gid):
    try:
        # Fetch project status updates
        updates = list(asana_client.project_statuses.get_project_statuses_for_project(project_gid, opt_fields="text"))
       
        if not updates:
            print("[INFO] No status updates found.")
            return 0, 0, 0
 
        # Get the latest status text
        latest_status = updates[0]["text"]
        print(f"[INFO] Latest Status: {latest_status}")  # Debugging: Check the latest status
       
        # Updated regex pattern to match task IDs in the new URL format
        task_ids = re.findall(r"https://app\.asana\.com/1/\d+/project/\d+/task/(\d+)", latest_status)
 
        if not task_ids:
            print("[INFO] No task links found in the status.")
            return 0, 0, 0
       
        print(f"[INFO] Task IDs extracted: {task_ids}")  # Debugging: Check the extracted task IDs
 
        # Counting total tasks and completed tasks
        total = len(task_ids)
        completed = 0
 
        # Loop through task IDs and check their completion status
        for tid in task_ids:
            try:
                task = asana_client.tasks.get_task(tid, opt_fields="completed")
                if task.get("completed"):
                    completed += 1
            except Exception as e:
                print(f"[ERROR] Failed to fetch task {tid}: {e}")
 
        # Calculate completion percentage
        percent = int((completed / total) * 100) if total else 0
        return total, completed, percent
 
    except Exception as e:
        print(f"[ERROR] Failed to fetch linked tasks in status update for project {project_gid}: {e}")
        return 0, 0, 0
 
# Call the function with the project GID
total_tasks, completed_tasks, completion_percentage = get_task_completion_from_status_links(project_gid)
 
# Print the result
print(f"Total tasks: {total_tasks}")
print(f"Completed tasks: {completed_tasks}")
print(f"Completion percentage: {completion_percentage}%")