from openai import OpenAI
from config import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)


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
    print(ask_chatgpt("幫我生五句話以內的獨角獸床邊故事，要小朋友的口吻，加入哥吉拉。"))
