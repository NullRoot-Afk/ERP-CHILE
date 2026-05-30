# Modelo de Base de Datos

Estrategia multi-tenant: **row-level isolation** con `tenant_id` en cada tabla.
Una sola base de datos para todos los tenants. Extensible a BD por tenant en Plan Empresa.

## Módulos y tablas

### Core / Plataforma
- `tenants` — empresas registradas
- `users` — usuarios por empresa (rol: owner / admin / user)
- `refresh_tokens` — tokens de renovación de sesión

### Subscripción & Billing
- `plans` — definición de planes (Gratis, Pyme, Pro, Empresa)
- `subscriptions` — subscripción activa por tenant + contador DTE mensual
- `audit_log` — registro de acciones para compliance

### Facturación SII
- `clientes` — receptores de DTE
- `proveedores` — emisores de documentos recibidos
- `folios_sii` — CAF por tipo de DTE (XML encriptado con Fernet)
- `documentos_tributarios` — DTEs emitidos (facturas, boletas, guías, NC, ND)

### Inventario
- `categorias` — jerarquía de categorías (self-reference)
- `productos` — catálogo con SKU, precios, código de barras
- `bodegas` — ubicaciones físicas de stock
- `stock` — saldo actual por producto/bodega (tabla snapshot)
- `movimientos_stock` — historial de entradas/salidas/ajustes

## Notas de implementación

**Folio SII con SELECT FOR UPDATE**
```python
# Siempre bloquear el registro antes de incrementar para evitar folios duplicados
folio = db.query(FolioSII).filter(...).with_for_update().first()
```

**Encriptación de certificados SII**
Los CAF y certificados `.pfx` se guardan encriptados con `cryptography.fernet`.
La `SII_CERT_ENCRYPTION_KEY` es un secreto de aplicación, nunca en el repo.

**Stock: siempre actualizar tabla `stock` + insertar en `movimientos_stock`**
Nunca calcules el stock actual sumando movimientos en producción.

## Diagrama DBML
Ver archivo `erp_saas_chile.dbml` en esta carpeta.
