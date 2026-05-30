from app.core.celery_app import celery_app


@celery_app.task
def verificar_stock_minimo(tenant_id: str):
    """
    Verifica productos bajo stock mínimo y genera alertas.
    """
    # TODO: implementar en Fase 1
    pass
