from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app import models,schemas,auth,database
from app.utils.email_alert import welcome_mail
router=APIRouter()

@router.post("/register",response_model=schemas.EmployeeResponse)
def register_employee(employee:schemas.EmployeeCreate, db:Session=Depends(database.get_db)):
    existing_user=db.query(models.Employee).filter(models.Employee.username==employee.username).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Username already exists")
    if db.query(models.Employee).filter(models.Employee.email==employee.email).first():
        raise HTTPException(status_code=400,detail="Email already exists")
    
    hashed_password=auth.hash_password(employee.password)
    new_employee=models.Employee(username=employee.username,password=hashed_password,email=employee.email,role=employee.role)
    new_employee.is_active=False
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    welcome_mail(new_employee.email,new_employee.username)
    return new_employee 

