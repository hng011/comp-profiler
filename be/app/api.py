from fastapi import APIRouter
from .Routers import Root, Insight

api_router = APIRouter()

api_router.include_router(Root.router, tags=["root"])
api_router.include_router(Insight.router, prefix="/insight", tags=["Insights"])