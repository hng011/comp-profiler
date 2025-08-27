from pydantic import BaseModel, HttpUrl


class InsightRequest(BaseModel):
    company_url: HttpUrl
    user_notes: str
    
class InsigtResponse(BaseModel):
    insight: str