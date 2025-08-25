import re
import os
import asana
from dotenv import load_dotenv
load_dotenv()
ASANA_TOKEN = os.getenv("ASANA_ACCESS_TOKEN")
asana_client = asana.Client.access_token(ASANA_TOKEN)
workspace_id = "1208832380740289"


def get_all_project_gids(workspace_gid):
    try:
        projects = asana_client.projects.get_projects_for_workspace(
            workspace_gid,
            opt_fields="gid,name"
        )
        return [{"name": p["name"], "gid": p["gid"]} for p in projects]
    except Exception as e:
        print(f"[ERROR] Couldn't fetch projects: {e}")
        return []

def get_task_completion_from_status_links(project_gid):
    try:
        updates = list(asana_client.project_statuses.get_project_statuses_for_project(
            project_gid, opt_fields="text"
        ))
        if not updates:
            return 0, 0, 0

        latest_status = updates[0]["text"]
        task_ids = re.findall(r"https://app\.asana\.com/1/\d+/project/\d+/task/(\d+)", latest_status)
        if not task_ids:
            return 0, 0, 0

        total = len(task_ids)
        completed = 0
        for tid in task_ids:
            try:
                task = asana_client.tasks.get_task(tid, opt_fields="completed")
                if task.get("completed"):
                    completed += 1
            except Exception as e:
                print(f"[ERROR] Failed to fetch task {tid}: {e}")

        percent = int((completed / total) * 100) if total else 0
        return total, completed, percent
    except Exception as e:
        print(f"[ERROR] Failed on project {project_gid}: {e}")
        return 0, 0, 0
    
from datetime import datetime

def get_tasks_completed_on_date(project_gid, target_date):
    try:
        tasks = asana_client.tasks.get_tasks_for_project(
            project_gid,
            opt_fields="name,completed,completed_at",
            completed_since=target_date.strftime("%Y-%m-%dT00:00:00Z")  # this is filtering some
        )

        result = []
        for task in tasks:
            if task.get("completed") and task.get("completed_at"):
                completed_at = datetime.fromisoformat(task["completed_at"].replace("Z", "+00:00"))
                if completed_at.date() == target_date.date():
                    result.append({
                        "name": task["name"],
                        "completed_at": completed_at
                    })

        return result

    except Exception as e:
        print(f"[ERROR] Failed to fetch tasks for project {project_gid}: {e}")
        return []

