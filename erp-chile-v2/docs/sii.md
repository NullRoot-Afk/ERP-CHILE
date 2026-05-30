# Integración SII — Decisiones técnicas

## Tipos de DTE implementados en Fase 1
| Código | Tipo                  | Uso                        |
|--------|-----------------------|----------------------------|
| 33     | Factura Electrónica   | Venta B2B con IVA          |
| 34     | Factura Exenta        | Venta B2B sin IVA          |
| 39     | Boleta Electrónica    | Venta B2C                  |
| 52     | Guía de Despacho      | Traslado de mercadería      |
| 56     | Nota de Débito        | Aumentar monto factura      |
| 61     | Nota de Crédito       | Anular o reducir factura    |

## Flujo de emisión de un DTE
1. Reservar folio con `SELECT FOR UPDATE`
2. Construir XML según esquema SII
3. Firmar XML con certificado digital del tenant
4. Encapsular en sobre de envío
5. Enviar a SII (async via Celery) → obtener `track_id`
6. Consultar estado por `track_id` hasta obtener Aceptado/Rechazado
7. Generar PDF y subir a S3
8. Enviar XML + PDF al cliente por email (SES)

## Ambientes SII
- **Certificación**: `maullin.sii.cl` — para pruebas, no tiene efectos tributarios
- **Producción**: `palena.sii.cl` — documentos reales

Controlar con variable `SII_AMBIENTE` en `.env`.
**Nunca cambiar a producción sin avisar al cliente.**

## Librerías clave
- `lxml` — construcción y parseo de XML
- `cryptography` — firma digital con certificado `.pfx`
- `httpx` — cliente HTTP async para llamadas a SII

## Referencias oficiales
- Resolución Exenta SII N°45 (2003) y modificaciones
- https://www.sii.cl/factura_electronica/
