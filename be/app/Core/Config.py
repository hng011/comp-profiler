from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    API_NAME: str            
    API_VERSION: str
    API_KEY: str             
    
    AI_API_KEY: str
    AI_API_ENDPOINT: str
    SYSTEM_PROMPT: str
    MAX_GENERATED_SUM: int
    
    ALLOWED_ORIGINS: List[str]
    ALLOWED_CREDENTIALS: bool
    ALLOWED_METHODS: List[str]   
    ALLOWED_HEADERS: List[str] 
    
    MAX_LEN_SCRAPER: int
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
settings = Settings()