from fastapi import APIRouter,status,Depends,HTTPException
from fastapi.responses import RedirectResponse
from database import get_db
from schemas import SignUpModel, LoginModel
from models import User, Account, Session as UserSession
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import session
from datetime import datetime, timedelta
import httpx
from oauth2_config  import (
    GOOGLE_OAUTH2_TOKEN_URL, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET,
    GOOGLE_REDIRECT_URI, GOOGLE_OAUTH2_USERINFO_URL
)


auth_routes = APIRouter()

@auth_routes.get("/login/google")
async def login_google():
    redirect_uri = f"https://accounts.google.com/o/oauth2/auth?client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&response_type=code&scope=openid%20email"
    return RedirectResponse(url=redirect_uri)
@auth_routes.get("/login/google/callback")
async def google_callback(code: str, db: session = Depends(get_db), authorize: AuthJWT = Depends()):
    try:
        # Lấy token từ Google
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
            access_token = token_data.get("access_token")

            # Lấy thông tin người dùng từ Google
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

        # Khởi tạo account
        account = db.query(Account).filter(Account.provider == "google", Account.provider_account_id == user_info.get("sub")).first()
        if not account:
            account = Account(
                user_id=user.id,
                type="oauth",
                provider="google",
                provider_account_id=user_info.get("sub"),
                refresh_token=token_data.get("refresh_token"),
                access_token=token_data.get("access_token"),
                expires_at=(datetime.utcnow() + timedelta(seconds=token_data.get("expires_in"))).timestamp(),
                token_type=token_data.get("token_type"),
                scope=token_data.get("scope"),
                id_token=token_data.get("id_token"),
                session_state=token_data.get("session_state")
            )
            db.add(account)
        else:
            account.refresh_token = token_data.get("refresh_token")
            account.access_token = token_data.get("access_token")
            account.expires_at = (datetime.utcnow() + timedelta(seconds=token_data.get("expires_in"))).timestamp()
            account.token_type = token_data.get("token_type")
            account.scope = token_data.get("scope")
            account.id_token = token_data.get("id_token")
            account.session_state = token_data.get("session_state")

        db.commit()

        # Tạo session cho user
        session_token = authorize.create_access_token(subject=user.id)
        session = UserSession(
            session_token=session_token,
            user_id=user.id,
            expires=datetime.utcnow() + timedelta(days=1)  # Session expires in 1 day
        )
        print("User ID:", user.id)
        print("Session Token:", session_token)
        print("Session Created:", session)

        db.add(session)
        db.commit()

        # Đặt cookie và chuyển hướng đến trang chủ
        response = RedirectResponse(url="http://localhost:3000/")
        response.set_cookie(key="access_token", value=session_token)
        return response

    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error occurred: {e.response.text}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

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