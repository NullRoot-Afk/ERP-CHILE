# ERP Chile 🇨🇱

ERP SaaS multi-tenant para pequeñas empresas de retail en Chile.
Facturación electrónica SII, inventario y punto de venta.

## Inicio rápido

```bash
# 1. Clonar y configurar variables de entorno
cp backend/.env.example backend/.env
# Editar backend/.env con tus valores

# 2. Levantar servicios con Docker
docker-compose up -d

# Backend:  http://localhost:8000
# API Docs: http://localhost:8000/docs
# Frontend: http://localhost:5173
```

## Estructura del proyecto

```
erp-chile/
├── backend/                  # FastAPI + Python 3.12
│   ├── app/
│   │   ├── api/v1/           # Endpoints REST
│   │   ├── core/             # Config, DB, Security, Celery
│   │   ├── middleware/       # Tenant middleware
│   │   ├── models/           # Modelos SQLAlchemy
│   │   ├── schemas/          # Schemas Pydantic v2
│   │   ├── services/         # Lógica de negocio (SII, PDF)
│   │   └── tasks/            # Tareas Celery async
│   ├── alembic/              # Migraciones de BD
│   └── tests/
├── frontend/                 # React 18 + TypeScript + Tailwind
│   └── src/
│       ├── components/       # ui/ (genéricos) + modules/ (por módulo)
│       ├── pages/            # auth, dashboard, facturacion, inventario
│       ├── services/         # Cliente HTTP (axios)
│       ├── store/            # Estado global (Zustand)
│       ├── hooks/            # Custom hooks (React Query)
│       └── types/            # TypeScript types/interfaces
├── infra/                    # Dockerfiles + CI/CD
│   └── .github/workflows/
├── docs/                     # Arquitectura, BD, SII
├── docker-compose.yml        # Desarrollo local
└── .gitignore
```

## Stack tecnológico

| Capa | Tecnología |
|------|-----------|
| Frontend | React 18, TypeScript, Tailwind CSS, React Query, Zustand |
| Backend | FastAPI, Python 3.12, SQLAlchemy 2.0, Pydantic v2 |
| Base de datos | PostgreSQL 16 |
| Caché / Colas | Redis 7 + Celery |
| Storage | AWS S3 |
| Email | AWS SES |
| Auth | JWT (30 min) + Refresh Token (7 días) |

## Roadmap

- **Fase 1** (meses 1-3): Autenticación multi-empresa, Facturación SII, Inventario
- **Fase 2** (meses 4-5): POS / Punto de Venta, Cuentas por cobrar/pagar
- **Fase 3** (meses 6+): Remuneraciones, CRM, Reportes con IA

## Documentación

- [Arquitectura](docs/arquitectura.md)
- [Modelo de BD](docs/database.md)
- [Integración SII](docs/sii.md)
- API Docs: http://localhost:8000/docs (solo en desarrollo)
