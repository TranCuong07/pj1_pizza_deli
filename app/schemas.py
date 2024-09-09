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
    lastUpdated: str

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


class WebhookData (BaseModel):
    id: Optional[str]
    gateway : str
    transaction_date : str
    accountNumber: str
    account_number :str
    sub_account : str
    amount_in :float
    amount_out :float
    accumulated :float
    code :str
    transaction_content : str
    reference_number : str
    body : str
    created_at: datetime
    
    class Config:
        orm_mode=True
    
    