from app.core.celery_app import celery_app


@celery_app.task(bind=True, max_retries=5, default_retry_delay=60)
def enviar_dte_sii(self, documento_id: str):
    """
    Envía un DTE al SII de forma asíncrona.
    Reintenta hasta 5 veces con 60 segundos de espera entre intentos.
    """
    # TODO: implementar en Fase 1
    pass


@celery_app.task(bind=True, max_retries=3, default_retry_delay=300)
def consultar_estado_dte(self, documento_id: str, track_id: str):
    """
    Consulta el estado de un DTE enviado al SII.
    """
    # TODO: implementar en Fase 1
    pass


@celery_app.task
def alertar_folios_bajos():
    """
    Tarea periódica: alerta cuando quedan menos de 50 folios disponibles.
    Ejecutar con celery beat cada 6 horas.
    """
    # TODO: implementar en Fase 1
    pass
