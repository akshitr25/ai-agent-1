import ollama

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

    response = ollama.chat(
        model='llama3',
        messages=chat_history
    )

    reply = response['message']['content']
    chat_history.append({"role": "assistant", "content": reply})

    return reply


if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        result = task_agent(user_input)
        print("\nAI:", result)