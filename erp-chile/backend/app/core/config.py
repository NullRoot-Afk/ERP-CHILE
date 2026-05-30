from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "ERP Chile"
    VERSION: str = "0.1.0"
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/erp_chile"
    REDIS_URL: str = "redis://localhost:6379"
    SECRET_KEY: str = "cambia-esto-en-produccion"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    AWS_BUCKET_NAME: str = ""
    AWS_ACCESS_KEY: str = ""
    AWS_SECRET_KEY: str = ""
    SII_AMBIENTE: str = "certificacion"  # o "produccion"

    class Config:
        env_file = ".env"

settings = Settings()
