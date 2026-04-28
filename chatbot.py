import anthropic

client = anthropic.Anthropic(api_key="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")

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a helpful assistant named Ethan Bot. you are friendly, consise, slightly funny and ultra cool.",
        messages=conversation_history
    )

    assistant_message = response.content[0].text

    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message

print("")
print("="*30)
print("  Welcome to Ethan Bot!")
print("="*30)
print("")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Ethan Bot: Deuces!")
        break
    response = chat(user_input)
    print("Ethan Bot: " + response)
    print("")
