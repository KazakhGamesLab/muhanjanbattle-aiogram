from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
REDIS_URL = os.getenv("REDIS_URL")
FASTAPI_HOST = os.getenv("FASTAPI_HOST")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
ADMINS = os.getenv("ADMINS")