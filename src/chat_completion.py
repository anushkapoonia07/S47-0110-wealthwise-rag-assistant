
import os
import logging
from pathlib import Path

from dotenv import load_dotenv
from openai import (
    OpenAI,
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APIStatusError,
)

# Load configuration from .env
load_dotenv()

BASE_URL = os.getenv("OPENAI_API_BASE_URL")
API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("CHAT_MODEL")

# Validate configuration
if not all([BASE_URL, API_KEY, MODEL]):
    raise ValueError(
        "Missing configuration. Check OPENAI_API_BASE_URL, "
        "OPENAI_API_KEY, and CHAT_MODEL in your .env file."
    )

# Set up logging
log_dir = Path("outputs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "chat.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)

# Create OpenAI-compatible client
client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
    timeout=120.0,
)

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant explaining technical concepts "
            "accurately and simply."
        ),
    },
    {
        "role": "user",
        "content": (
            "In artificial intelligence, what does RAG stand for? "
            "Explain Retrieval-Augmented Generation and how it works "
            "in a knowledge-base assistant. Do not invent another expansion."
        ),
    },
]


def main():
    try:
        logger.info("Outgoing messages: %s", messages)

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
        )

        answer = response.choices[0].message.content

        logger.info("Incoming response: %s", response.model_dump_json())
        logger.info("Token usage: %s", response.usage)

        print("\nAssistant response:")
        print(answer)

        print("\nToken usage:")
        print(response.usage)

        print(f"\nModel: {response.model}")
        print(f"Log saved to: {log_dir / 'chat.log'}")

    except AuthenticationError:
        print("Authentication error (401): Check your API key.")

    except RateLimitError:
        print("Rate limit error (429): Too many requests or quota exceeded.")

    except APIConnectionError:
        print(
            "Connection error: Make sure Ollama is running "
            "at http://localhost:11434."
        )

    except APIStatusError as error:
        print(f"API error ({error.status_code}): The request failed.")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
