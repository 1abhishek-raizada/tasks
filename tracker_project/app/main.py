from fastapi import *
from sqlalchemy.orm import Session
from datetime import timedelta
from . import models,schemas,crud,database,oauth2
import jwt
import datetime
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import text
from . routers import authentication
from fastapi.openapi.models import OAuthFlowAuthorizationCode, OAuthFlowImplicit
from fastapi.openapi.models import OAuthFlowAuthorizationCode


#initializing the fastapi
app=FastAPI()
app.include_router(authentication.router)

#Database session dependency
def get_db_session(db:Session=Depends(database.get_db)):
    return db


# Include OAuth2 token authentication in Swagger UI
app.openapi_schema["components"]["securitySchemes"] = {
    "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
    }
}
@app.get("/openapi.json")
def get_openapi():
    openapi_schema = app.openapi()
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    return openapi_schema
@app.get("/some_protected_route")
def some_protected_route(current_user: str = Depends(oauth2.get_current_user)):
    return {"message": "This is a protected route", "user": current_user}







@app.get("/test-db")
def test_db(db:Session=Depends(database.get_db)):
    try:
        #Try executing a simple query
        db.execute(text("SELECT 1"))
        return {"message":"Database connection is successfull"}
    except Exception as e:
        return {"error":str(e)}




#API FOR EMPLOYEE REGISTRATION
@app.post("/register")    
def register_employee(employee:schemas.EmployeeCreate,db:Session=Depends(database.get_db)):
    db_employee=crud.create_employee(db=db,employee=employee)
    if not db_employee:
        raise HTTPException(status_code=400,detail="Error creating employee")
    return {"message":"Employee registered successfully"}



#API for tracking activity (mouse clicks and keyboard press)
@app.post("/track_activity")
async def track_activity(activity:schemas.ActivityLogCreate,db:Session=Depends(database.get_db)):
    employee=db.query(models.Employee).filter(models.Employee.id==activity.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404,detail="Employee not found!")
    
    new_activity=models.ActivityLog(
        employee_id=activity.employee_id,
        activity_type=activity.activity_type,
        status=activity.status
    )
    db.add(new_activity)
    db.commit()
    return {"message":"Activity log created!","activity":activity}

@app.get("/employee/{employee_id}/activity_logs")
async def get_activity_logs(employee_id: int, db: Session = Depends(get_db_session)):
    # Fetch employee with their activity logs
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return {"employee": employee.username, "activity_logs": [log.activity_type for log in employee.activity_logs]}

    