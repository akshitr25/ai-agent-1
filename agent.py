from openai import OpenAI
from dotenv import load_dotenv
import os
from config import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def get_response(user_input):
    # TOOL TRIGGER
    if "total time" in user_input.lower():
        return estimate_total_time(user_input)
    chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )

    reply = response.choices[0].message.content

    chat_history.append({"role": "assistant", "content": reply})

    return reply

def estimate_total_time(tasks_text):
    # very simple logic for now
    return "Estimated total time: 25-30 hours"