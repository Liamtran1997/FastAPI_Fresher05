from pydantic import BaseModel, fields, EmailStr
from typing import Optional


class Address(BaseModel):
    street: str
    city: str
    country: str


class Student(BaseModel):
    id: str
    name: Optional[str] = None
    address: Optional[Address] = None
    email: str


