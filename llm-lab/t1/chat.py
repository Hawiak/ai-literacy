import anthropic
from anthropic.types import MessageParam, TextBlock
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

MODEL = "claude-sonnet-5-5"
SYSTEM = "Je bent een vriendelijke en behulpzame assistent, maar je wilt het niet hebben over katten. Als iemand over katten begint, zeg je NEE"


def main() -> None:
    total_in = total_out = 0
    history: list[MessageParam] = []
    print("Type /reset om opnieuw te beginnen en /stop om te stoppen")
    while True:
        user = input("\n> ").strip()
        if user == "/stop":
            break
        if user == "/reset":
            history.clear()
            total_in = total_out = 0
            print("Geschiedenis gewist")
            continue
        if not user:
            continue

        history.append({"role": "user", "content": user})
        with client.messages.stream(
            model=MODEL,
            max_tokens=1000,
            system=SYSTEM,
            messages=history,
        ) as stream:
            for chunk in stream.text_stream:
                print(chunk, end="", flush=True)
            final = stream.get_final_message()

        history.append(
            {
                "role": "assistant",
                "content": "".join(
                    b.text for b in final.content if isinstance(b, TextBlock)
                ),
            }
        )
        total_in += final.usage.input_tokens
        total_out += final.usage.output_tokens
        print(
            f"\n[tokens in {final.usage.input_tokens} uit={final.usage.output_tokens}]"
            f" | sessie in={total_in} uit={total_out} | stop={final.stop_reason}"
        )


if __name__ == "__main__":
    main()
