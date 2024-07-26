# Other modules
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE_PATH = BASE_DIR / ".env.dev"
load_dotenv(ENV_FILE_PATH)

# Flask
SECRET_KEY = os.environ.get("SECRET_KEY", "YOUR-FALLBACK-SECRET-KEY")
DATABASE_URI = "mysql://iwpSHiGDXghiwKJjLQHQgeTDGPvfbbho@viaduct.proxy.rlwy.net:17828/railway"
FLASK_DEBUG = True
# Ratelimit
RATELIMIT_ENABLED = os.environ.get("RATELIMIT_ENABLED", "False") == "True"
RATELIMIT_STORAGE_URI = os.environ.get("RATELIMIT_STORAGE_URI", "memory://")
# Caching
CACHE_ENABLED = True
CACHE_TYPE = 'RedisCache'
CACHE_REDIS_HOST = 'viaduct.proxy.rlwy.net'
CACHE_REDIS_PORT = 50622
CACHE_REDIS_PASSWORD = 'kPHvUeUfZDMEMmbmtIKqrwGfmdGNNvfQ'
CACHE_REDIS_DB = 0
CACHE_DEFAULT_TIMEOUT = 300  # Cache timeout in seconds
CACHE_STORAGE_URL = "redis://:kPHvUeUfZDMEMmbmtIKqrwGfmdGNNvfQ@viaduct.proxy.rlwy.net:50622/0"
CACHE_EXEMPTED_ROUTES = [
    "/api/auth/",
]


class DevConfig:
    # Flask
    TESTING = True
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    STATIC_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING = False
    SECRET_KEY = SECRET_KEY
    # Database
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    # Ratelimit
    RATELIMIT_ENABLED = RATELIMIT_ENABLED
    RATELIMIT_STORAGE_URI = RATELIMIT_STORAGE_URI
    RATELIMIT_STRATEGY = "fixed-window"  # or "moving-window"
    RATELIMIT_IN_MEMORY_FALLBACK_ENABLED = True
    RATELIMIT_HEADERS_ENABLED = True
    # Configure cache
