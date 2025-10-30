import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")
if not OPENAI_API_BASE:
    raise ValueError("OPENAI_API_BASE is not set")


def main():
    print("Hello from langchain-course!")
    print(OPENAI_API_KEY)
    print(OPENAI_API_BASE)


if __name__ == "__main__":
    main()
