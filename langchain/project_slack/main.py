from asana_data import get_all_project_gids, get_task_completion_from_status_links,workspace_id
from generate_summary import generate_daily_report,get_human_readable_date
from raw_slack import get_prioritized_projects_from_slack,post_report_to_slack

import json
import os
import datetime

PRIORITY_FILE = "weekly_priorities.json"

def save_priorities(priorities):
    with open(PRIORITY_FILE, "w") as f:
        json.dump({
            "week_start": str(datetime.date.today()),
            "priorities": priorities
        }, f)

def load_priorities():
    with open(PRIORITY_FILE, "r") as f:
        return json.load(f)["priorities"]  

def is_monday():
    
    return datetime.datetime.today().weekday() == 0           

def save_report_to_file(summary_text):
    folder = "daily_report"
    os.makedirs(folder, exist_ok=True)  # Create folder if not exists

    filename = f"{get_human_readable_date()}.txt"
    filepath = os.path.join(folder, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(summary_text)

    print(f"Report saved to: {filepath}")


def main():
    # Step 1: Slack priorities
    if is_monday():
        prioritized_names = get_prioritized_projects_from_slack()
        save_priorities(prioritized_names)
        print("Slack priorities fetched and saved.")
    else:
        prioritized_names = load_priorities()
        print(" Using saved priorities from Monday.")

    # # Step 2: Fetch all Asana projects
    # projects = get_all_project_gids(workspace_id)
    # project_completion_data = []
    
    # for project in projects:
    #     name = project["name"]
    #     gid = project["gid"]
    #     total, completed, percent = get_task_completion_from_status_links(gid)
    #     print(f"{name}: {completed}/{total} ({percent}%)")
    #     project_completion_data.append({"name": name, "percent": percent})

    # # Step 3: Helper to clean Asana names
    # def clean_internal_name(name):
    #     return name.replace("Internal - ", "").replace("Internal-", "").strip()

    # asana_lookup = {
    #     clean_internal_name(p["name"]).lower(): p["percent"]
    #     for p in project_completion_data
    # }

    # final_projects = []
    # for slack_name in prioritized_names:
    #     clean_name = slack_name.strip()
    #     percent = asana_lookup.get(clean_name.lower(), "--")
    #     final_projects.append({
    #         "name": clean_name,
    #         "percent": percent
    #     })

    # # Step 4: Generate + Post + Save report
    # summary = generate_daily_report(final_projects)
    # post_report_to_slack(summary)
    # save_report_to_file(summary)

#recent working main
# def main():
#     # Step 1: Get Slack priorities first
#     prioritized_names = get_prioritized_projects_from_slack()

#     # Step 2: Fetch all Asana projects
#     projects = get_all_project_gids(workspace_id)
#     project_completion_data = []
    
#     for project in projects:
#         name = project["name"]
#         gid = project["gid"]
#         total, completed, percent = get_task_completion_from_status_links(gid)
#         print(f"{name}: {completed}/{total} ({percent}%)")
#         project_completion_data.append({"name": name, "percent": percent})

#     # Step 3: Helper to clean project name
#     def clean_internal_name(name):
#         return name.replace("Internal - ", "").replace("Internal-", "").strip()

#     # Step 4: Match Slack names to Asana projects
#     asana_lookup = {
#         clean_internal_name(p["name"]).lower(): p["percent"]
#         for p in project_completion_data
#     }

#     final_projects = []
#     for slack_name in prioritized_names:
#         clean_name = slack_name.strip()
#         percent = asana_lookup.get(clean_name.lower(), "--")
#         final_projects.append({
#             "name": clean_name,
#             "percent": percent
#         })

#     # Step 5: Generate and save report
#     summary = generate_daily_report(final_projects)
#     save_report_to_file(summary)

#     post_report_to_slack(summary)


# def main():
#     projects = get_all_project_gids(workspace_id)
#     project_completion_data = []
    
#     for project in projects:
#         name = project["name"]
#         gid = project["gid"]
#         total, completed, percent = get_task_completion_from_status_links(gid)
#         print(f"{name}: {completed}/{total} ({percent}%)")
#         project_completion_data.append({"name": name, "percent": percent})

#     def is_internal_project(name):
#         return name.lower().startswith("internal")  # catches both 'Internal -' and 'Internal-'

#     def clean_internal_name(name):
#         return name.replace("Internal - ", "").replace("Internal-", "").strip()
#     # Create a lookup map from cleaned Asana project names
#     asana_lookup = {
#         clean_internal_name(p["name"]).lower(): p["percent"]
#         for p in project_completion_data
#     }
#     final_projects=[]
#     for slack_name in prioritized_names:  # uncleaned names from Slack
#         clean_name = slack_name.strip()
#         percent = asana_lookup.get(clean_name.lower(), "--")
#         final_projects.append({
#             "name": clean_name,
#             "percent": percent
#         })
#     # Filter only internal projects
#     internal_projects = [
#         {"name": clean_internal_name(p["name"]), "percent": p["percent"]}
#         for p in project_completion_data
#         if is_internal_project(p["name"])
#     ]

#     summary = generate_daily_report(internal_projects)
#     slack_projects = get_prioritized_projects_from_slack()
#     slack_projects
#     save_report_to_file(summary)
#     print("\nDaily Summary:\n")
#     print(summary)

if __name__ == "__main__":
    main()
