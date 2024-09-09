from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)


def chat_with_gpt(user_prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model="gpt-4o-2024-05-13",
        )
        content = response.choices[0].message.content
        return content
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Chat GPT:", response)
