from pydantic import BaseModel
from datetime import datetime

class Bus(BaseModel):
    id: str
    route_id: str
    current_stop_index: int = 0
    last_updated_at: datetime
