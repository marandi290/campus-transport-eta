from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.bus_service import update_checkpoint

router = APIRouter()

class CheckpointRequest(BaseModel):
    stop_name: str

@router.post("/buses/{bus_id}/checkpoint")
def update_bus_checkpoint(bus_id: str, payload: CheckpointRequest):
    try:
        update_checkpoint(bus_id, payload.stop_name)
        return {"message": "Checkpoint updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
