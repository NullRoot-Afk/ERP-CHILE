from uuid import uuid4
from sqlalchemy import String, Integer, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import UUID
class Base(DeclarativeBase):
    pass
class Tennant(Base):
    __tablename__ = "tenants"
    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    rut_empresa: Mapped[str] = mapped_column(String(255), nullable=False)
    razon_social: Mapped[str] = mapped_column(String(255), nullable=False)
    giro: Mapped[str] = mapped_column(String(255), nullable=True)
    direccion: Mapped[str] = mapped_column(String(255), nullable=True)
    comuna: Mapped[str] = mapped_column(String(255), nullable=True)
    ciudad: Mapped[str] = mapped_column(String(255), nullable=True)
    region: Mapped[str] = mapped_column(String(255), nullable=True)
    email_sii: Mapped[str] = mapped_column(String(255), nullable=False)
    cert_sii_path: Mapped[str] = mapped_column(String(255), nullable=True)
    cert_sii_password_encrypted: Mapped[str] = mapped_column(String(255), nullable=True)
    ambiente_sii: Mapped[str] = mapped_column(String(255), nullable=False)
    plan: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True

