from app.core.celery_app import celery_app


@celery_app.task(bind=True, max_retries=3, default_retry_delay=120)
def enviar_dte_por_email(self, documento_id: str, email_destino: str):
    """
    Envía el PDF y XML de un DTE al cliente por email via AWS SES.
    """
    # TODO: implementar en Fase 1
    pass
