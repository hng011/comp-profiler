import httpx
from app.Core.Config import settings

async def ai_summarizer(scraped_text: str, user_notes: str | None) -> str:
    url = settings.AI_API_ENDPOINT
    system_prompt = settings.SYSTEM_PROMPT
    
    user_prompt = f"""
Based on the following company information and user notes, perform two tasks:
1. Generate exactly {settings.MAX_GENERATED_SUM} characters including space of company profile summary and make it concise and do not include the character count in the output.”.
2. Analyze how well the company aligns with the user's notes and provide a score from 1 to 10, along with a brief justification.
---
COMPANY INFORMATION: {scraped_text}
---
USER'S NOTES: {user_notes}

# Template for Summarization Result (Do not include anything outside the template below)
---
## **Company Profile**:
<content>

## **Alignment Score**:
<content> (7/10) for example

## **Justification**:
<content>
---
    """
    
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": settings.AI_API_KEY
    }
    
    payloads = {
        "contents": [
            {
                "role": "model",
                "parts": [
                    {"text":system_prompt}      
                ]
            },
            {
                "role": "user",
                "parts": [
                    {"text": user_prompt}
                ]
            }
        ]
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url=url, headers=headers, json=payloads)
            
        text = response.json()
        return text["candidates"][0]["content"]["parts"][0]["text"]
        
    except httpx.RequestError as e:
        return e