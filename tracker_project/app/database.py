from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from fastapi import HTTPException
from . import models

SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:King#123@localhost:3306/employee_tracker"

engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"host":"localhost"})
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
models.Base.metadata.create_all(bind=engine)

Base=declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db  # Provides the session to FastAPI routes
    except SQLAlchemyError as e:
        db.rollback()  # If any error happens, rollback the transaction
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")  # Handle database-related errors
    finally:
        db.close()  # Close the database session