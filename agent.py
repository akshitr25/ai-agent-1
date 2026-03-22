from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_response(user_input):
    plan = planner_agent(user_input)

    if "time" in user_input.lower():
        time_info = executor_agent(plan)
        # REMOVE any "Total Time" from LLM output
        # plan = plan.split("Total Time")[0]
        return plan + "\n\n" + time_info

    return plan


def planner_agent(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
                Break the user's goal into structured tasks.

                Return:
                1. Task name
                2. Time required
                3. Priority

                DO NOT calculate or mention total time.
                """
            },
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content


def executor_agent(plan):
    return estimate_total_time(plan)

import re

def estimate_total_time(plan):
    times = re.findall(r'(\d+)\s*hour', plan)
    total = sum(map(int, times))

    if total == 0:
        return "Estimated total time: Not enough data"

    return f"Estimated total time: {total} hours"