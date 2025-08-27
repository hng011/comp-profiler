from . import *
from app.Core.Config import settings
from app.Helpers.WebsiteScraper import company_profile_scraper

@pytest.mark.asyncio
async def test_company_profile_scraper():
    result = await company_profile_scraper(test_url)
    
    isinstance(result, str)
    assert len(result) <= settings.MAX_LEN_SCRAPER
    
    print(f"len_text: {len(result)}\nContent: {result}")