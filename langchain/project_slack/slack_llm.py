from openai import OpenAI
from raw_slack import fetch_recent_priority_messages
client = OpenAI()

def extract_priorities_with_llm(priority_messages):
    prompt = f"""
You are given a set of Slack messages where teams list their project priorities. Extract only the **project names** from the content. Ignore vague tasks, instructions, or empty messages. Return a clean Python list of project names, exactly as they appear.

Messages:
{priority_messages}

Output:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    extracted = response.choices[0].message.content.strip()
    print("✅ Extracted priorities:\n", extracted)
    return eval(extracted)

