import asana
import os
from dotenv import load_dotenv

load_dotenv()
ASANA_TOKEN = os.getenv("ASANA_ACCESS_TOKEN")
# WORKSPACE_GID='1208832380740289'
WORKSPACE_GID='1208832380740289'
client = asana.Client.access_token(ASANA_TOKEN)

# Step 3: Function to get all project task completion status
def get_project_completion_summary(workspace_gid):
    report = {}

    # Step 3.1: Get all projects in workspace
    projects = client.projects.get_projects_for_workspace(
        workspace_gid,
        params={"archived": False, "opt_fields": "name,gid"}
    )

    for project in projects:
        name = project["name"]
        pid = project["gid"]
        print(f"🔍 Checking project: {name} ({pid})")

        try:
            tasks = list(client.tasks.find_by_project(pid, {"opt_fields": "completed"}))
            
            total = len(tasks)
            completed = sum(1 for task in tasks if task.get("completed"))

            percent = round((completed / total) * 100, 2) if total else 0.0

            report[name] = {
                "completed": completed,
                "total": total,
                "percent": percent
            }

        except Exception as e:
            report[name] = {
                "completed": 0,
                "total": 0,
                "percent": 0.0,
                "error": str(e)
            }

    return report


summary=get_project_completion_summary(WORKSPACE_GID)

for proj, stats in summary.items():
    print(f"{proj}: {stats['completed']}/{stats['total']} ({stats['percent']}%)")