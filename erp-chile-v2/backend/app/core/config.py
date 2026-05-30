from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    APP_NAME: str = "ERP Chile"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"  # development | production

    # Base de datos — requerido, sin default
    DATABASE_URL: str = Field(..., description="PostgreSQL connection string")
    REDIS_URL: str = Field(..., description="Redis connection string")

    # Seguridad — requerido, sin default (explota si no está en .env)
    SECRET_KEY: str = Field(..., description="JWT secret key — mínimo 32 caracteres")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30       # 30 min — estándar para ERP financiero
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # AWS
    AWS_REGION: str = "us-east-1"
    AWS_BUCKET_NAME: str = ""
    AWS_ACCESS_KEY: str = ""
    AWS_SECRET_KEY: str = ""

    # SES
    SES_FROM_EMAIL: str = ""

    # SII
    SII_AMBIENTE: str = "certificacion"         # certificacion | produccion
    SII_CERT_ENCRYPTION_KEY: str = Field(
        ..., description="Fernet key para encriptar certificados SII de clientes"
    )

    # CORS — lista separada por comas en el .env
    CORS_ORIGINS: str = "http://localhost:5173"

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
