from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, database, auth
from datetime import timedelta

router = APIRouter()

def format_seconds(seconds):
    return str(timedelta(seconds=int(seconds)))

@router.get("/daily-summary/{employee_id}")
def get_daily_summary(
    employee_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.Employee = Depends(auth.get_current_user),
):
    if current_user.role != "manager":
        return {'error':"Only Managers can view this!"}
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    summary = db.query(models.DailyWorkingHours).filter_by(employee_id=employee_id).first()
    if not summary:
        raise HTTPException(status_code=404, detail="No daily summary found for this employee")
    
    formatted_time = format_seconds(summary.total_active_seconds)

    return {
        "employee": employee.username,
        "date": str(summary.date),
        "active_time": formatted_time
    }
