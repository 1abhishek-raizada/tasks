from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)
    role=Column(String(100),default="employee")
    email=Column(String(100),unique=True,nullable=True)
    is_active = Column(Boolean, default=True)
    last_active = Column(DateTime, default=datetime.utcnow)

    activities = relationship("ActivityLog", back_populates="employee")
    working_hours=relationship("WorkingHours",back_populates="employee")
    daily_hours=relationship("DailyWorkingHours",back_populates="employee")
    screenshots=relationship("Screenshot", back_populates="employee")

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    action=Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)

    employee = relationship("Employee", back_populates="activities")

class WorkingHours(Base):
    __tablename__="working_hours"
    id=Column(Integer,primary_key=True,index=True)
    employee_id=Column(Integer,ForeignKey("employees.id"))
    total_active_seconds=Column(Integer,default=0)
    last_active_time=Column(DateTime,nullable=True)
    inactivity_alert_sent=Column(Integer,default=0)

    employee=relationship("Employee",back_populates="working_hours")    

class DailyWorkingHours(Base):
    __tablename__="daily_working_hours"

    id=Column(Integer,primary_key=True, index=True)
    employee_id=Column(Integer, ForeignKey("employees.id"))
    date= Column(Date,nullable=False)
    total_active_seconds=Column(Float, default=0.0)

    employee=relationship("Employee",back_populates="daily_hours")    

class Screenshot(Base):
    __tablename__="screenshots"

    id=Column(Integer,primary_key=True,index=True)
    employee_id=Column(Integer,ForeignKey("employees.id"))
    timestamp=Column(DateTime,default=datetime.utcnow)
    file_path=Column(String(255))

    employee=relationship("Employee", back_populates="screenshots")
