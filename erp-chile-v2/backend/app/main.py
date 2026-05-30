from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings
from app.middleware.tenant import tenant_middleware
from app.api.v1 import auth, facturas, productos

app = FastAPI(
    title="ERP Chile API",
    description="API para ERP SaaS orientado a retail chileno",
    version=settings.VERSION,
    docs_url="/docs" if settings.ENVIRONMENT == "development" else None,
    redoc_url="/redoc" if settings.ENVIRONMENT == "development" else None,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Multi-tenant middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=tenant_middleware)

# Routers Fase 1
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(facturas.router, prefix="/api/v1/facturas", tags=["facturación"])
app.include_router(productos.router, prefix="/api/v1/productos", tags=["inventario"])


@app.get("/health", tags=["sistema"])
def health():
    return {"status": "ok", "version": settings.VERSION, "env": settings.ENVIRONMENT}
