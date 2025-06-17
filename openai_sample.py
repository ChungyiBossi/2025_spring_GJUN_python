from openai import OpenAI
client = OpenAI(api_key="MY_API_KEY")


def ask_chatgpt(prompt: str) -> str:
    """
    Ask ChatGPT with a given prompt and return the response text.
    """
    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )
    return response.output_text


if __name__ == "__main__":
    ask_chatgpt("幫我生五句話以內的獨角獸床邊故事。")
