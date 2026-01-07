import os

class BaseConfig:
    """Base configuration class."""
    SECRET_KEY = os.getenv("SECRET_KEY", "fdsafasd")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(os.path.dirname(__file__), "image_pool"))
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    TESTING = False
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    """Development configuration class."""
    DEBUG = True

class TestingConfig(BaseConfig):
    """Testing configuration class."""
    TESTING = True
    DEBUG = True

class ProductionConfig(BaseConfig):
    DATABASE_URL = os.getenv("DATABASE_URL")