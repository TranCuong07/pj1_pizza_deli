# oauth2_config.py

import os
from dotenv import load_dotenv

# Nạp biến môi trường từ file .env
load_dotenv()

# Lấy thông tin từ biến môi trường
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
GOOGLE_OAUTH2_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_OAUTH2_USERINFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

SO_TAI_KHOAN = os.getenv("SO_TAI_KHOAN")
NGAN_HANG = os.getenv("NGAN_HANG")
TEMPLATE= os.getenv("TEMPLATE")
DOWNLOAD = os.getenv("DOWNLOAD")