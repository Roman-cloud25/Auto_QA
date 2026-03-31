import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    BASE_URL = os.getenv("BASE_URL", "http://5.101.50.27:8000")

    AUTH_USERNAME = os.getenv("AUTH_USERNAME", "harrypotter")
    AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", "expelliarmus")

    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))

    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


    @classmethod
    def validate(cls) -> bool:
        """
        Checks for the presence of required environment variables.
        Returns:
        bool: True if all required variables are present
        """
        required_vars = ["BASE_URL", "AUTH_USERNAME", "AUTH_PASSWORD"]
        missing_vars = [var for var in required_vars if not getattr(cls, var)]

        if missing_vars:
            print(f"Warning: Missing environment variables: {missing_vars}")
            return False
        return True