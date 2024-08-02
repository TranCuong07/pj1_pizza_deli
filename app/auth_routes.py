from fastapi import APIRouter,status,Depends
from database import get_db
from schemas import SignUpModel, LoginModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import session


auth_routes = APIRouter()

@auth_routes.get('/')
async def  hello():
    return {"hello"}

@auth_routes.post('/signup',status_code=status.HTTP_201_CREATED)
async def signup(user:SignUpModel,db:session = Depends(get_db)):
    db_email = db.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Tai khoan mail da ton tai"                  
                            )
    
    db_username = db.query(User).filter(User.username == user.username).first()

    if db_username is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="username da ton tai"                  
                             )
    new_user=User(
        username =user.username,
        password = generate_password_hash(user.password),
        email = user.email,
        is_active = user.is_active,
        is_staff = user.is_staff
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#login
@auth_routes.post('/login',status_code=200)
async def login(user:LoginModel,authorize:AuthJWT=Depends(),db:session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.username == user.username).first()
        if db_user and check_password_hash(db_user.password,user.password):
            access_token = authorize.create_access_token(subject=db_user.username)
            refresh_token = authorize.create_refresh_token(subject=db_user.username)

            response ={
                "access_token":access_token,
                "refresh_token":refresh_token
            }

            return jsonable_encoder(response)
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Tài khoản không tồn tại hoặc mật khẩu không đúng"
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Kết nối lỗi hoặc lỗi không xác định"
                            )

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
