from datetime import datetime
import openai

def get_human_readable_date():
    today = datetime.today()
    day = today.day
    suffix = (
        "th" if 11 <= day <= 13 else
        {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    )
    return today.strftime(f"%-d{suffix} %B %Y (%A)")

def generate_daily_report(projects):
    report_date = get_human_readable_date()
    project_lines = "\n".join([f"{i+1}. {p['name']} – {p['percent']}%" for i, p in enumerate(projects)])

    user_prompt = f"""Below is the task completion data for a list of projects, extracted from Asana and shared in a daily Slack update.

Generate a natural language summary using clear. HIGHLIGHT ALL PROJECTS EXACTLY AS PROVIDED, INCLUDING THEIR COMPLETION RATES. DO NOT OMIT ANY PROJECTS UNDER ANY CIRCUMSTANCES.

DO NOT RANK PROJECTS OR REORDER THEM BASED ON COMPLETION RATE. MAINTAIN THE ORIGINAL ORDER STRICTLY.
DO NOT GENERATE ANY EXTRA COMMENTS REGARDING ANY PROJECT. 
GENERATE ONLY THE OUTPUT ACCORDING TO THE BELOW FORMAT.
Use a tone that’s motivational and clear. Format the summary for easy readability in Slack.

format:
Daily Update ({report_date})
{project_lines}

Example:
Daily Update (30 june 2025)(Monday):
1. New Haven         44%
2. Sandbox            9%
3. Canal              0%
4. Aptar              0%
5. Bankwell           0%
6. Lifford            0%
7. Bioforce           0%
8. Molecular Designs  0%
9. Mavrix             0%
10. Mudflap          33%
11. Quility           0%
12. DevOps            0%

"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a project status analyst writing summaries for Slack."},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message["content"]
