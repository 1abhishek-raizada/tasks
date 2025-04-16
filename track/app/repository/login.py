from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app import models,schemas,auth,database
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter()

@router.post("/login")
def login(employee:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(database.get_db)):
    user=db.query(models.Employee).filter(models.Employee.username==employee.username).first()
    if not user or not auth.verify_password(employee.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires=timedelta(minutes=30)
    access_token = auth.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    # models.Employee.is_active=False
    # db.commit()
    return {"access_token":access_token,"token_type":"bearer"}
