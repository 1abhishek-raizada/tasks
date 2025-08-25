from slack_sdk import WebClient
import openai
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
BOT_USER_ID = os.getenv("BOT_USER_ID")  
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

slack_client = WebClient(token=SLACK_BOT_TOKEN)


def post_report_to_slack(report_text):
    try:
        slack_client.chat_postMessage(
            channel=os.getenv("SLACK_CHANNEL_ID"),
            text=f"*Daily Update:*\n```{report_text}```"
        )
        print("Report posted to Slack.")
    except Exception as e:
        print(f"Failed to post to Slack: {e}")

def fetch_recent_messages(limit=30):
    try:
        response = slack_client.conversations_history(
            channel=os.getenv("SLACK_CHANNEL_ID"),
            limit=limit
        )
        messages = response["messages"]

        bot_user_id = os.getenv("BOT_USER_ID")
        if not bot_user_id:
            print(" BOT_USER_ID not set in environment. All messages will be included.")

        # Filter and return non-empty text messages, excluding bot’s own messages
        raw_texts = [
            msg["text"]
            for msg in messages
            if msg.get("text") and msg.get("user") != bot_user_id and "bot_id" not in msg
        ]

        print(f"Fetched {len(raw_texts)} filtered messages from Slack.")
        return raw_texts

    except Exception as e:
        print(f" Slack API Error: {e}")
        return []

def extract_priorities_with_llm(priority_messages):
    formatted_msgs = "\n".join(f"- {msg}" for msg in priority_messages)

    prompt = f"""
You are a Slack Message Analyzer tasked with identifying project priorities for the week from team conversations.

Below is a list of Slack messages from the team:
{formatted_msgs}

Your task:
- Extract project names mentioned as priorities or areas of focus for the current week.
- Messages may include numbered lists, bullet points, inline mentions, or informal phrasing like "top projects" or "this week's focus".
- Ignore noise, duplicates, status-only messages, or unrelated content.
...
Only extract *project names*, not individual tasks, features, updates, or one-off initiatives.

Return ONLY project names in this Python list format:
["New Haven", "Bioforce", "Canal"]
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    extracted = response["choices"][0]["message"]["content"].strip()

    # Clean code block wrapping if LLM returns markdown
    if extracted.startswith("```"):
        extracted = extracted.strip("```").replace("python", "").strip()

    print("Extracted priorities:\n", extracted)

    try:
        return eval(extracted)
    except Exception as e:
        print(f" Failed to parse extracted priorities: {e}")
        return []


def get_prioritized_projects_from_slack():
    msgs = fetch_recent_messages()
    return extract_priorities_with_llm(msgs)

