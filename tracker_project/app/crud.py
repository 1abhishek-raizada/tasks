from sqlalchemy.orm import Session
from . import models,schemas
from passlib.context import CryptContext

pwd_context=CryptContext(schemes=['bcrypt'], deprecated="auto")

def get_employee_by_username(db: Session, username: str):
    return db.query(models.Employee).filter(models.Employee.username == username).first()

def hash_password(password:str):
    return pwd_context.hash(password)

def create_employee(db:Session, employee:schemas.EmployeeCreate):
    hashed_password=hash_password(employee.password)
    db_employee=models.Employee(username=employee.username,password=hashed_password)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def track_activity(db:Session,activity:schemas.ActivityLogCreate):
    db_activity=models.ActivityLog(
        employee_id=activity.employee_id,
        activity_type=activity.activity_type,
        status=activity.status
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity