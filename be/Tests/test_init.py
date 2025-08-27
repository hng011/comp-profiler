from . import *
from fastapi.testclient import TestClient
from app.main import app
from app.Core.Config import settings

client = TestClient(app)

def test_get_root_no_api_key():
    response = client.get("/api/v1/")
    assert response.status_code == 401
    
def test_get_root_with_api_key():
    headers = {
        "X-Api-Key": settings.API_KEY,
    }
    
    response = client.get("/api/v1/", headers=headers).json()
    assert isinstance(response, dict)
    assert response["status"] == "ok"