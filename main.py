from openai import OpenAI
import os

# Set your API key (better: use environment variable)
client = OpenAI(api_key="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")

chat_history = [
    {
        "role": "system",
        "content": """
        You are a strict productivity assistant.

        Your job:
        - Break goals into tasks
        - Keep answers concise
        - Do NOT give general knowledge or long explanations
        - Always return structured tasks with:
          1. Task name
          2. Time required
          3. Priority
        """
    }
]

def task_agent(user_input):
    chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )

    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})

    return reply


if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        result = task_agent(user_input)
        print("\nAI:", result)