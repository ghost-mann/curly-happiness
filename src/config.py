import os
from dotenv import load_dotenv

load_dotenv()

VISUALCROSSING_API_KEY = os.getenv('')
AIRVISUAL_API_KEY = os.getenv('')

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DEFAULT_CITY = os.getenv('DEFAULT_CITY', 'Nairobi')
DEFAULT_COUNTRY = os.getenv('DEFAULT_COUNTRY', 'Kenya')
DEFAULT_START_DATE = os.getenv('DEFAULT_START_DATE', '2024-01-01')
DEFAULT_END_DATE = os.getenv('DEFAULT_END_DATE', '2024-12-31')