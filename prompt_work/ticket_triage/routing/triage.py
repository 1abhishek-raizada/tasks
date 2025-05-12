from fastapi import APIRouter
from pydantic import BaseModel
from ..services.triage_engine import run_all_prompts

router=APIRouter()

class TicketInput(BaseModel):
    message:str



@router.post("/triage")
async def triage_ticket(ticket: TicketInput):
    result=run_all_prompts(ticket.message)
    return result

