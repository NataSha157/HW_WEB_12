from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel, EmailStr, Field

from src.schemas.user import UserResponse


class ContactSchema(BaseModel):
    firstname: str = Field(min_length=2, max_length=50)
    lastname: str = Field(min_length=2, max_length=50)
    e_mail: EmailStr
    birthday: date
    add_data: Optional[str] = Field(default=None, max_length=250)


class ContactUpdateSchema(ContactSchema):
    add_data: str


class ContactResponse(BaseModel):
    id: int = 1
    firstname: str
    lastname: str
    e_mail: EmailStr
    birthday: date
    add_data: str
    created_at: datetime | None
    update_at: datetime | None
    user: UserResponse | None

    class Config:
            from_attributes = True

