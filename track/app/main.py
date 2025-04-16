from fastapi import FastAPI
from app.repository import register,login,activity,manager,show_activity
from app.database import engine,Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.repository.activity import start_cleanup_scheduler  # or wherever you placed it

import os


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

screenshot_dir=os.path.join("app","screenshots")
app.mount("/screenshots",StaticFiles(directory=screenshot_dir),name="screenshots")



app.include_router(register.router,prefix="/auth",tags=["Authentication"])
app.include_router(login.router,prefix="/auth",tags=["Authentication"])
app.include_router(activity.router, prefix="/activity",tags=["Activity Tracking"])
app.include_router(manager.router,prefix="/manager",tags=["Manager Dashboard"])
app.include_router(show_activity.router,prefix="/manager",tags=["Manager Dashboard"])
@app.get("/")
def root():
    return {"message":"Welcome to Employee Trackng System!"}

@app.on_event("startup")
def startup_event():
    start_cleanup_scheduler()
    