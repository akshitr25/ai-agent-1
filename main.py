from agent import get_response
def run():
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        result = task_agent(user_input)
        print("\nAI:", result)
if name=="__main__":
    run()