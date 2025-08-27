from . import *
from fastapi.testclient import TestClient
from app.main import app
from app.Core.Config import settings

client = TestClient(app)

def test_generate_insights_success():
    payload = {"company_url": test_url, "user_notes": ""}
    headers = {"X-API-Key": settings.API_KEY}
    response = client.post(f"/api/v1/insight/generate", headers=headers, json=payload)
    
    assert str(response.status_code) == "200"
    
    response_data: dict = response.json()
    
    assert len(response_data["insight"]) <= settings.MAX_GENERATED_SUM
    
    print(response_data)

def test_generate_insights_no_api_key():
    payload = {"company_url": test_url, "user_notes": ""}
    response = client.post("/api/v1/insights/generate", json=payload)
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid or missing API Key"}