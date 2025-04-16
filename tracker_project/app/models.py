from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base=declarative_base()




class Employee(Base):
    __tablename__="employees"
    
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(255),unique=True,index=True)
    password=Column(String(255))
    role=Column(Enum('manager','employee', name="role_enum"))
    created_at=Column(TIMESTAMP,default=func.now(),nullable=False)

    activity_logs=relationship("ActivityLog",back_populates="employees")
    working_hours=relationship("WorkingHour",back_populates="employees")


class ActivityLog(Base):
    __tablename__="activity_logs"

    id=Column(Integer,primary_key=True,index=True)
    employee_id=Column(Integer,ForeignKey('employees.id'))
    activity_type=Column(Enum('click','keyboard'))
    timestamp=Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'),nullable=False)
    status=Column(Enum('active','inactive'),default='active')

    employees=relationship("Employee",back_populates="activity_logs")

class WorkingHour(Base):
    __tablename__="working_hours"

    id=Column(Integer,primary_key=True,index=True)
    employee_id=Column(Integer,ForeignKey('employees.id'))
    total_hours=Column(DECIMAL(10,2),default=0)

    employees=relationship("Employee",back_populates="working_hours")
    
