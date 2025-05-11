from baml_client import b
from baml_client.types import MyUserMessage

def main():
    messages: MyUserMessage = []
    while True:
        user_input = input("Enter you message (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the chat.")
            break
        messages.append({"role": "user", "content": user_input})
        response = b.ChatWithLLM(messages)
        print("LLM response:", response)
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
