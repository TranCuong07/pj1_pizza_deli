from pydantic import BaseModel, Field
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int] = Field(None, description="Unique ID of the user")
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

