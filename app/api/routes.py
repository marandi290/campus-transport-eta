from fastapi import APIRouter, HTTPException
from app.services.bus_service import get_bus_status

router = APIRouter()

@router.get("/{route_id}/bus-status")
def bus_status(route_id: str):
    try:
        return get_bus_status(route_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
