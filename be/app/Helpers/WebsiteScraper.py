import httpx
from app.Core.Config import settings
from bs4 import BeautifulSoup

async def company_profile_scraper(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
        
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=10, follow_redirects=True)
            response.raise_for_status()            
            
        soup = BeautifulSoup(response.content, features="html.parser")
        paragraphs = soup.find_all('p')
        
        if not paragraphs:
            raise httpx.RequestError
        
        full_text = " ".join(p.get_text(strip=True) for p in paragraphs)
        
        return full_text[:settings.MAX_LEN_SCRAPER]
        
    except httpx.RequestError as e:
        return f"Error: Could not retrieve the webpage. {e}"