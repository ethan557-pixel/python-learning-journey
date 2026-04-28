import anthropic

client = anthropic.Anthropic(api_key="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")

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Say hello and tell me one fun fact about Nashville!"}
    ]
)

print(message.content[0].text)