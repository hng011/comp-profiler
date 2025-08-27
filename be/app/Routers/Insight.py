from fastapi import APIRouter, HTTPException
from app.Schemas.InsightSchema import InsightRequest, InsigtResponse
from app.Helpers.WebsiteScraper import company_profile_scraper
from app.Helpers.AISummarizer import ai_summarizer

router = APIRouter()

@router.post("/generate", response_model=InsigtResponse)
async def generate_insight(request: InsightRequest):
    scraped_text = await company_profile_scraper(str(request.company_url))
    if "Error:" in scraped_text:
        return HTTPException(status_code=400, detail=scraped_text)
    
    ai_response = await ai_summarizer(
        scraped_text=scraped_text, 
        user_notes=request.user_notes or None
    )
    
    return InsigtResponse(insight=ai_response)