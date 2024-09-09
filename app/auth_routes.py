from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import RedirectResponse
from database import get_db
from schemas import SignUpModel, LoginModel
from models import User, Account, Session as UserSession
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import httpx
from oauth2_config import (
    GOOGLE_OAUTH2_TOKEN_URL, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,
    GOOGLE_REDIRECT_URI, GOOGLE_OAUTH2_USERINFO_URL
)

auth_routes = APIRouter()

@auth_routes.get("/login/google")
async def login_google():
    redirect_uri = f"https://accounts.google.com/o/oauth2/auth?client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&response_type=code&scope=openid%20email"
    return RedirectResponse(url=redirect_uri)

@auth_routes.get("/login/google/callback")
async def google_callback(code: str, db: Session = Depends(get_db), authorize: AuthJWT = Depends()):
    try:
        # Bước 1: Lấy token từ Google
        async with httpx.AsyncClient() as client:
            token_response = await client.post(
                GOOGLE_OAUTH2_TOKEN_URL,
                data={
                    "code": code,
                    "client_id": GOOGLE_CLIENT_ID,
                    "client_secret": GOOGLE_CLIENT_SECRET,
                    "redirect_uri": GOOGLE_REDIRECT_URI,
                    "grant_type": "authorization_code",
                },
            )
            if token_response.status_code != 200:
                raise HTTPException(status_code=token_response.status_code, detail="Failed to fetch token from Google")
            token_data = token_response.json()
            id_token = token_data.get("id_token")
            access_token = token_data.get("access_token")

            # Bước 2: Xác minh token ID từ Google
            verified_token = await verify_google_token(id_token)

            # Kiểm tra các trường quan trọng của token
            if verified_token['aud'] != GOOGLE_CLIENT_ID:
                raise HTTPException(status_code=400, detail="Token was not issued for this application")
            if verified_token['iss'] not in ["accounts.google.com", "https://accounts.google.com"]:
                raise HTTPException(status_code=400, detail="Token was not issued by Google")

            # Bước 3: Lấy thông tin người dùng từ Google
            user_info_response = await client.get(
                GOOGLE_OAUTH2_USERINFO_URL,
                headers={"Authorization": f"Bearer {access_token}"},
            )
            if user_info_response.status_code != 200:
                raise HTTPException(status_code=user_info_response.status_code, detail="Failed to fetch user info from Google")
            user_info = user_info_response.json()

        email = user_info.get("email")

        # Kiểm tra người dùng trong cơ sở dữ liệu
        user = db.query(User).filter(User.email == email).first()
        if not user:
            # Tạo người dùng mới nếu chưa tồn tại
            user = User(email=email, name=user_info.get("name"), image=user_info.get("picture"))
            db.add(user)
            db.commit()
            db.refresh(user)

        # Khởi tạo JWT Token của bạn
        session_token = authorize.create_access_token(subject=str(user.id), expires_time=timedelta(days=1))

        # Tạo session và lưu vào cơ sở dữ liệu nếu cần
        user_session = UserSession(
            session_token=session_token,
            user_id=user.id,
            expires=datetime.utcnow() + timedelta(days=1)
        )
        db.add(user_session)
        db.commit()

        # Thiết lập cookie và phản hồi
        response = RedirectResponse(url="http://localhost:3000/")
        response.set_cookie(key="access_token", value=session_token, max_age=60 * 60 * 24)  # Cookie hợp lệ trong 24 giờ
        return response

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error occurred: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

async def verify_google_token(id_token: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={id_token}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Invalid token")
        return response.json()


@auth_routes.get('/refresh')
async def refresh(authorize: AuthJWT = Depends(),):
    try:
        authorize.jwt_refresh_token_required()
        current_user = authorize.get_jwt_subject()
        access_token = authorize.create_access_token(subject=current_user)
        response = {"new_access_token": access_token}
        return jsonable_encoder (response)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Khong xac dinh duoc token")