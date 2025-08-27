from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
def root(request: Request):
    return {
        "title": request.app.title,
        "version": request.app.version,
        "status": "ok",    
    }