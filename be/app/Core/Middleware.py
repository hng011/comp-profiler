from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware 
from starlette.responses import JSONResponse
from starlette import status
from fastapi.middleware.cors import CORSMiddleware
from .Config import settings


class ApiKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get("X-API-Key")

        if not api_key or api_key != settings.API_KEY:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid or missing API Key"}
            )
            
        response = await call_next(request)
        return response

def setup_middleware(app: FastAPI) -> None:
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins       = settings.ALLOWED_ORIGINS,
        allow_credentials   = settings.ALLOWED_CREDENTIALS,
        allow_methods       = settings.ALLOWED_METHODS,
        allow_headers       = settings.ALLOWED_HEADERS,
    )
    
    app.add_middleware(ApiKeyMiddleware)