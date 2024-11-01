# app/config.py
from pydantic_settings import BaseSettings  # Import BaseSettings from pydantic-settings

class Settings(BaseSettings):
    # Define your settings variables here
    DATABASE_URL: str  # This can be your PostgreSQL connection string
    GEMINI_API_KEY: str  # Add the Gemini API key

    class Config:
        env_file = ".env"  # Load environment variables from .env file
        extra = "forbid"  # Prevent extra fields from being passed

settings = Settings()  # Create an instance of Settings
