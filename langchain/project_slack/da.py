from datetime import datetime
from asana_data import asana_client, ASANA_TOKEN
from main import workspace_id

def get_all_projects(workspace_gid):
    projects = asana_client.projects.get_projects_for_workspace(
        workspace_gid,
        opt_fields="gid,name"
    )
    return [{"name": p["name"], "gid": p["gid"]} for p in projects]

def get_tasks_completed_on_date(project_gid, target_date):
    try:
        tasks = asana_client.tasks.get_tasks_for_project(
            project_gid,
            opt_fields="name,completed,completed_at"
        )

        result = []
        for task in tasks:
            if task.get("completed") and task.get("completed_at"):
                completed_at = datetime.fromisoformat(task["completed_at"].replace("Z", "+00:00"))
                if completed_at.date() <= target_date.date():
                    result.append({
                        "name": task["name"],
                        "completed_at": completed_at
                    })

        return result

    except Exception as e:
        print(f"[ERROR] Project {project_gid}: {e}")
        return []

def get_all_tasks_done_on_date(workspace_gid, target_date):
    report = {}
    all_projects = get_all_projects(workspace_gid)

    for proj in all_projects:
        tasks_done = get_tasks_completed_on_date(proj["gid"], target_date)
        if tasks_done:
            report[proj["name"]] = tasks_done

    return report

from datetime import datetime

target_day = datetime(2025, 6, 30)
completed_tasks_report = get_all_tasks_done_on_date(workspace_id, target_day)

for project, tasks in completed_tasks_report.items():
    print(f"\n📁 {project}")
    for task in tasks:
        print(f"   ✅ {task['name']} at {task['completed_at'].strftime('%H:%M')}")
