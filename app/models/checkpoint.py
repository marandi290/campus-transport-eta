from pydantic import BaseModel
from datetime import datetime

class CheckpointUpdate(BaseModel):
    bus_id: str
    stop_name: str
    timestamp: datetime
