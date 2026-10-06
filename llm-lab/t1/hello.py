import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "Tell me about the history of Anthropic"}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
print("tokens", response.usage.input_tokens, "in", response.usage.output_tokens, "uit")
print("stop_reason:", response.stop_reason)
