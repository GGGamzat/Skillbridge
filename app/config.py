from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    DERIBIT_API_URL: str = "https://www.deribit.com/api/v2/public/"

    class Config:
        env_file = ".env"


settings = Settings()