from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int

    class Config:
        env_file = ".env"

settings = Settings()