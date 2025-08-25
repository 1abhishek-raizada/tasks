import openai
from datetime import datetime

def get_human_readable_date():
    today = datetime.today()
    day = today.day
    suffix = (
        "th" if 11 <= day <= 13 else
        {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    )
    formatted_date = today.strftime(f"%-d{suffix} %B %Y (%A)")
    return formatted_date

def generate_daily_report(projects):
    report_date = get_human_readable_date()

    project_lines = "\n".join([f"{i+1}. {p['name']} – {p['percent']}%" for i, p in enumerate(projects)])

    user_prompt = f"""
Below is the task completion data for a list of projects, extracted from Asana and shared in a daily Slack update.

Generate a natural language summary using clear, encouraging language. Highlight the top performing projects (above 30%), those with low progress (1–30%), and those with 0% completion.

Use a tone that’s motivational and clear. Format the summary for easy readability in Slack.

### Date: {report_date}

Project Completion Data:
{project_lines}

Summary:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are a helpful project status analyst writing summaries for Slack."},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message["content"]
