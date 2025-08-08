from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Core settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Default admin user
    DEFAULT_ADMIN_USERNAME: str = "admin"
    DEFAULT_ADMIN_PASSWORD: str = "admin123"

    # Server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    # Application metadata
    APP_NAME: str = "AI算法管理平台"
    VERSION: str = "1.0.0"

    # Database
    DATABASE_URL: str = "sqlite:///./ai_manager.db"

    # CORS
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1", "0.0.0.0"]

    # API behavior
    DEVICE_API_TIMEOUT: int = 30
    MAX_CONCURRENT_REQUESTS: int = 10

    # File handling
    UPLOAD_DIR: str = "./uploads"
    MAX_FILE_SIZE: int = 10485760  # 10 MB

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "./logs/app.log"

    class Config:
        env_file = [".env", "../.env"]
        env_file_encoding = 'utf-8'

settings = Settings()