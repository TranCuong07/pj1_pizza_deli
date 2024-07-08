from fastapi import APIRouter,status
from database import Session,engine
from schemas import SignUpModel
from models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash

session=Session(bind=engine)

auth_routes = APIRouter()

@auth_routes.get('/')
async def  hello():
    return {"test chức năng auth"}

@auth_routes.post('/signup',response_model=SignUpModel,
                  status_code=status.HTTP_201_CREATED
                  )
async def signup(user:SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Tai khoan mail da ton tai"                  
                            )
    
    db_username = session.query(User).filter(User.username == user.username).first()

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

    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user