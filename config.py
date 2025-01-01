from pydantic_settings import BaseSettings
import os

os.chdir(os.path.dirname(__file__))

class Config():
    # GPT_MODEL: str = os.getenv("GPT_MODEL")
    # EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL")
    # OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    
    # PG_DATABASE_URL: str = os.getenv("PG_DATABASE_URL")
    # PG_DATABASE_NAME: str = os.getenv("PG_DATABASE_NAME")
    # PG_DATABASE_USER: str = os.getenv("PG_DATABASE_USER")
    # PG_DATABASE_PASSWORD: str = os.getenv("PG_DATABASE_PASSWORD")
    # PG_DATABASE_HOST: str = os.getenv("PG_DATABASE_HOST")
    # PG_DATABASE_PORT: str = os.getenv("PG_DATABASE_PORT")

    GPT_MODEL: str = "gpt-4o"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    OPENAI_API_KEY: str = open("../data/API_KEY", "r").read()

    PG_DATABASE_USER: str = "postgres"
    PG_DATABASE_PASSWORD: str = "postgres1016"
    PG_DATABASE_HOST: str = "192.168.0.47"
    PG_DATABASE_PORT: str = "55432"
    PG_DATABASE_NAME: str = "test"

    PG_DATABASE_URL: str = f"postgresql://{PG_DATABASE_USER}:{PG_DATABASE_PASSWORD}@{PG_DATABASE_HOST}:{PG_DATABASE_PORT}/{PG_DATABASE_NAME}"

config = Config()
