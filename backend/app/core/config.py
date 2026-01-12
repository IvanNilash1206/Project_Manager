from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Project Management System"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    DATABASE_URL: str
    SECRET_KEY: str
    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
