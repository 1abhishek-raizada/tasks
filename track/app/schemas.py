from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class EmployeeCreate(BaseModel):
    username: str
    password: str
    email   : EmailStr
    role    : Optional[str]="employee"      #defining the default as employee

class EmployeeLogin(BaseModel):
    username: str
    password: str

class EmployeeResponse(BaseModel):
    id: int
    username: str
    is_active: bool
    last_active: datetime

    class Config:
        from_attributes = True

class ActivityLogResponse(BaseModel):
    timestamp: datetime
