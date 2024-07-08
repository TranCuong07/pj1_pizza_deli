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
        from_attributes = True
        json_schema_extra = {
            'example': {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }