import os

from dotenv import load_dotenv

load_dotenv()


DATABASE_URL: str = f""
DATABASE_ECHO: bool = True
ALGORITHM: str = "RS256"


def get_public_key() -> str:
    with open("shared_data/jwtRS256.key.pub", "r") as key:
        return key.read()

public_key = get_public_key()


DATABASE_URL: str = (f"postgresql+asyncpg://{os.getenv("MESSAGES_DATABASE_USERNAME")}:{os.getenv("MESSAGES_DATABASE_PASSWORD")}"
                     f"@{os.getenv("MESSAGES_DATABASE_HOST")}:{os.getenv("MESSAGES_DATABASE_PORT")}/{os.getenv("MESSAGES_DATABASE_NAME")}")
DATABASE_ECHO: bool = False
