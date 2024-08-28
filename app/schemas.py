from pydantic import BaseModel, Field,datetime_parse
from typing import Optional,List
from datetime import datetime
from enum import Enum

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
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_secure: bool = False  # Set this to False for local development
    authjwt_cookie_csrf_protect: bool = False  # Tắt bảo vệ CSRF cho cookie trong môi trường phát triển



class LoginModel(BaseModel):
    username: str
    password: str

class ProductModel(BaseModel):
    id:str
    title: str
    img: str
    price: float
    optionTitle: str
    quantity: int


class CartData(BaseModel):
    products: List[ProductModel]
    totalPrice: float
    timestamp: str

class PaymentStatus(str, Enum):
    UNPAID = "Unpaid"
    PAID = "Paid"
    CANCELLED = "Cancelled"
    REFUNDED = "Refunded"
    
class OrderModel(BaseModel):
    id: Optional[str]
    created_at: Optional[datetime] = None
    price: float
    products: List[ProductModel]
    status: Optional[str] = "PENDING"
    intent_id: Optional[str] = None
    user_email: str
    payment_status: PaymentStatus = PaymentStatus.UNPAID

    class Config:
        orm_mode = True

class OrderCreateModel(BaseModel):
    price: float
    products: List[ProductModel]
    user_email: str
    payment_status: PaymentStatus = PaymentStatus.UNPAID

    class Config:
        orm_mode = True

class OrderModelStatus(BaseModel):
    order_status : Optional[str]="PENDING"
    
    class Config:
        orm_mode=True
        schema_extra = {
            'example': {
                "order_status": "PENDING"
            }
        }



    