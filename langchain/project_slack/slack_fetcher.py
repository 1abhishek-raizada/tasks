import os
import requests
from typing import List


def get_priorities_from_slack()->List[str]:
    SLACK_BOT_TOKEN=os.getenv("SLACK_BOT_TOKEN")
    CHANNEL_ID=os.getenv("SLACK_CHANNEL_ID")

    headers={
        "Authorization":f"Bearer {SLACK_BOT_TOKEN}"
        
    }
    params={
        "channel":CHANNEL_ID,
        "limit":50              #here we are setting the limit for the number of messages to fetch
    
    }

    response=requests.get("https://slack.com/api/conversations.history",headers=headers, params=params)
    data=response.json()


    if not data.get("ok"):
        raise Exception(f"Slack API error: {data.get('error')}")
    
    messages=data.get("messages",[])
    # print("🧪 Raw Slack messages:")
    # for m in messages:
    #     print(m.get("text", ""), "\n")
    #extracting the priorites with a simple rule: lines starting with 'PRIORITIES'
    priorites=[]
    for msg in messages:
        text=msg.get("text","")
        if text.startswith("PRIORITIES"):
            priority=text.replace("PRIORITIES", "").strip()
            priorites.append(priority)

    return priorites        