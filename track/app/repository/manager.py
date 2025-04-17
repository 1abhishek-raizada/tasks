from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from app import models,database,auth
from datetime import date,datetime
from typing import List,Optional
router=APIRouter()

@router.get("/working-hours/{employee_id}")
def get_employee_working_hours(
    employee_id:int,
    db:Session=Depends(database.get_db),
    current_user:models.Employee=Depends(auth.get_current_user),
):
    "fetching total active hours for an employee (Manager Access)"
    #first ensuring the current user is  manager
    manager=db.query(models.Employee).filter(models.Employee.username==current_user.username,models.Employee.role=="manager").first()
    if not manager:                     
        return {"error":"Only Managers can view this."}
    
    working_hours=db.query(models.WorkingHours).filter(models.WorkingHours.employee_id==employee_id).first()
    if not working_hours:
        return {"message":"No activity recorded for this employee."}
    
    total_hours=round(working_hours.total_active_seconds/3600, 2) #converting the seconds to hours
    return {"employee_id":employee_id,"total_active_hours":total_hours,}




 


@router.get("/employees")
def get_all_employees(
    db: Session = Depends(database.get_db),
    current_user: models.Employee=Depends(auth.get_current_user),  # Only managers allowed
):
    print(current_user)  
    if current_user.role != "manager":
        raise HTTPException(status_code=403, detail="Only managers can view this")
    employees = db.query(models.Employee).all()
    return employees
   
@router.get("/screenshots")
def get_screenshots(
    employee_id: Optional[int] = Query(None),
    date: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1),
    grouped: Optional[bool] = Query(False),
    db: Session = Depends(database.get_db),
    current_user: models.Employee = Depends(auth.get_current_user),
):
    if current_user.role != 'manager':
        raise HTTPException(status_code=403, detail="Only managers can view this.")

    query = db.query(models.Screenshot)

    if employee_id:
        query = query.filter(models.Screenshot.employee_id == employee_id)

    if date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
            start = datetime.combine(parsed_date, datetime.min.time())
            end = datetime.combine(parsed_date, datetime.max.time())
            query = query.filter(models.Screenshot.timestamp.between(start, end))
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    query = query.order_by(models.Screenshot.timestamp.desc())
    total = query.count()

    # Apply pagination only if not grouped
    if not grouped:
        offset = (page - 1) * limit
        query = query.offset(offset).limit(limit)

    results = query.all()
    base_url = "http://localhost:8000/screenshots"

    if grouped:
        grouped_result = {}
        for shot in results:
            shot_date = shot.timestamp.date().isoformat()
            if shot_date not in grouped_result:
                grouped_result[shot_date] = []

            relative_path = shot.file_path.replace("\\", "/").split("screenshots/")[-1]
            preview_url = f"{base_url}/{relative_path}"

            grouped_result[shot_date].append({
                "timestamp": shot.timestamp.isoformat(),
                "employee_id": shot.employee_id,
                "preview_url": preview_url,
                "file_path": shot.file_path
            })
        return grouped_result

    else:
        return {
            "total": total,
            "page": page,
            "limit": limit,
            "screenshots": [
                {
                    "employee_id": shot.employee_id,
                    "timestamp": shot.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "image_url": f"{base_url}/{shot.file_path.replace('app/screenshots/', '')}"
                }
                for shot in results
            ]
        }
