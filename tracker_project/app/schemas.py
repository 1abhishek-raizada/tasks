from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id      :int
    username:str
    role    :str

class Login(BaseModel):
    username:str
    password:str

class EmployeeCreate(BaseModel):
    username:str             
    password:str
    role    :str  #manager or employee

class ActivityLogCreate(BaseModel):
    employee_id:int
    activity_type:str
    status:str      

class WorkingHour(BaseModel):
    employee_id:int
    total_hours: float
    
class TokenData(BaseModel):
    username:Optional[str]=None           