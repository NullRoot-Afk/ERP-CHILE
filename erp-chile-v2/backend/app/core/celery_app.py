from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "erp_chile",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=[
        "app.tasks.sii_tasks",
        "app.tasks.email_tasks",
        "app.tasks.stock_tasks",
    ],
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="America/Santiago",
    enable_utc=True,
    # Reintentos automáticos ante fallos de red con SII
    task_acks_late=True,
    task_reject_on_worker_lost=True,
)
