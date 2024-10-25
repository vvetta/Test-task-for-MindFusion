
ALGORITHM: str = "RS256"
ACCESS_TOKEN_LIFE_TIME_MINUTES: int = 60


def get_private_key() -> str:
    with open("src/certs/jwtRS256.key", "r") as key:
        return key.read()


def get_public_key() -> str:
    with open("src/certs/jwtRS256.key.pub", "r") as key:
        return key.read()


private_key = get_private_key()
public_key = get_public_key()


USERS_SERVICE_HOST = "127.0.0.1"
USERS_SERVICE_PORT = 8080
USERS_SERVICE_URL = f"http://{USERS_SERVICE_HOST}:{USERS_SERVICE_PORT}/users/"

