from pydantic import BaseModel, Field
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] 
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode=True
        schema_extra = {
            'example': {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }

class Setting(BaseModel):
    authjwt_secret_key: str ='c81b9060d8051ec08ded9b5e92af08b6521fc975c6b5ac45be0bfff0b5d7ac8a'

class LoginModel(BaseModel):
    username: str
    password: str

class OrderModel(BaseModel):
    id : Optional[int]
    quantity : int
    order_status : Optional[str]="PENDING"
    pizza_size : Optional[str] ="SMALL"
    user_id : Optional[int]
    
    class Config:
        orm_mode=True
        schema_extra = {
            'example': {
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }

class OrderModelStatus(BaseModel):
    order_status : Optional[str]="PENDING"
    
    class Config:
        orm_mode=True
        schema_extra = {
            'example': {
                "order_status": "PENDING"
            }
        }