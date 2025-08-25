import os
from dotenv import load_dotenv

# Load your SLACK_BOT_TOKEN and SLACK_CHANNEL_ID from .env
load_dotenv()

from slack_fetcher import get_priorities_from_slack  # or paste the function inline here

if __name__ == "__main__":
    try:
        priorities = get_priorities_from_slack()
        print("✅ Priorities extracted from Slack:")
        for i, p in enumerate(priorities, 1):
            print(f"{i}. {p}")
    except Exception as e:
        print(f"❌ Error: {e}")
