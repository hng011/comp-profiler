from . import *
from app.Core.Config import settings
from app.Helpers.AISummarizer import ai_summarizer
from app.Helpers.WebsiteScraper import company_profile_scraper

@pytest.mark.asyncio
async def test_ai_summarizer():
    text_scrap = await company_profile_scraper(test_url)
    text_sum = await ai_summarizer(text_scrap, user_notes=None)
    
    isinstance(text_sum, str)
    assert len(text_sum) <= settings.MAX_GENERATED_SUM
    
    print(text_sum)