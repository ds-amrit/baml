class MyUserMessage{
    role "user" | "assistant"
    content string
}

function ChatWithLLM(messages: MyUserMessage[]) -> string {
    client "openai/gpt-4o-mini"
    prompt #"
        Reply to the following messages in a friendly and helpful manner, based on the conversation
        {% for message in messages %}
        {{ _.role(message.role) }}: {{ message.content }}
        {% endfor %}

        Answer:
    "#
}

test TestName {
    functions [ChatWithLLM]
    args   {
        messages [
            { role "user", content "Hello, how are you?" },
            { role "assistant", content "I'm doing well, thank you!" } 
        ]
    }
}