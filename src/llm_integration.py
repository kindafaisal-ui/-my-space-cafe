import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_content(prompt: str, provider: str = "openai", max_tokens: int = 1000) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found! Check your .env file.")
    client = OpenAI(api_key=api_key)
    print(f"  🤖 Generating with OpenAI...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def generate_generic(topic: str) -> str:
    generic_prompt = f"Write an Instagram caption for a café about: {topic}"
    return generate_content(generic_prompt)

if __name__ == "__main__":
    print("Testing OpenAI connection...\n")
    result = generate_content("Say exactly: 'API connection successful!' and nothing else.")
    print(f"Result: {result}")
