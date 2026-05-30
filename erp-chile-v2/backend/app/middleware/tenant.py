from fastapi import Request, HTTPException, status
from jose import JWTError
from app.core.security import decode_token


async def tenant_middleware(request: Request, call_next):
    """
    Extrae tenant_id del JWT y lo inyecta en request.state.
    Rutas públicas (login, register, health) se saltan el check.
    """
    PUBLIC_PATHS = {"/", "/api/v1/auth/login", "/api/v1/auth/register", "/docs",
                    "/redoc", "/openapi.json", "/health"}

    if request.url.path in PUBLIC_PATHS:
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no proporcionado",
        )

    token = auth_header.split(" ")[1]
    try:
        payload = decode_token(token)
        tenant_id = payload.get("tenant_id")
        user_id = payload.get("sub")
        if not tenant_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token sin tenant_id",
            )
        request.state.tenant_id = tenant_id
        request.state.user_id = user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
        )

    return await call_next(request)
