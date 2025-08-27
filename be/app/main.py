from fastapi import FastAPI
from .api import api_router
from .Core.Middleware import setup_middleware
from .Core.Config import settings

app = FastAPI(
    name=settings.API_NAME,
    version=settings.API_VERSION,
)

setup_middleware(app)

app.include_router(api_router, prefix="/api/v1")