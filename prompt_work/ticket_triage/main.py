from fastapi import FastAPI
from ticket_triage.routing.triage import router as triage_router

app=FastAPI(title="Smart Ticket Triage System")

app.include_router(triage_router,prefix="/api")