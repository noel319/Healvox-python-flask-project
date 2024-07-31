# Other modules
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE_PATH = BASE_DIR / ".env.dev"
load_dotenv(ENV_FILE_PATH)

# Flask
SECRET_KEY = os.environ.get("SECRET_KEY", "YOUR-FALLBACK-SECRET-KEY")
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:iwpSHiGDXghiwKJjLQHQgeTDGPvfbbho@viaduct.proxy.rlwy.net:17828/railway"
FLASK_DEBUG = True


# Caching
CACHE_ENABLED = True
CACHE_TYPE = 'RedisCache'
CACHE_REDIS_HOST = 'viaduct.proxy.rlwy.net'
CACHE_REDIS_PORT = 50622
CACHE_REDIS_PASSWORD = 'kPHvUeUfZDMEMmbmtIKqrwGfmdGNNvfQ'
CACHE_REDIS_DB = 0
CACHE_DEFAULT_TIMEOUT = 300  # Cache timeout in seconds
CACHE_STORAGE_URL = "redis://default:kPHvUeUfZDMEMmbmtIKqrwGfmdGNNvfQ@viaduct.proxy.rlwy.net:50622/0"
SQLALCHEMY_TRACK_MODIFICATIONS=False
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
    SECRET_KEY = "sjddlfghd123"
    SECRET_PASSWORD_SALT = "very-important"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:iwpSHiGDXghiwKJjLQHQgeTDGPvfbbho@viaduct.proxy.rlwy.net:17828/railway"
    FLASK_DEBUG = True
    # Caching
    CACHE_ENABLED = True
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = 'viaduct.proxy.rlwy.net'
    CACHE_REDIS_PORT = 50622
    CACHE_REDIS_PASSWORD = 'kPHvUeUfZDMEMmbmtIKqrwGfmdGNNvfQ'
    CACHE_REDIS_DB = 0
    CACHE_DEFAULT_TIMEOUT = 300  # Cache timeout in seconds
    CACHE_STORAGE_URL = "redis://default:kPHvUeUfZDMEMmbmtIKqrwGfmdGNNvfQ@viaduct.proxy.rlwy.net:50622/0"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    CACHE_EXEMPTED_ROUTES = [
    "/api/auth/",
    ]
    # Mail Configuration
    MAIL_SERVER = 'live.smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'api'
    MAIL_PASSWORD = '74e4569cbe22d7a27007139ab983b203'
    MAIL_DEFAULT_SENDER = 'demomailtrap.com'