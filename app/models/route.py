from pydantic import BaseModel
from typing import List

class Route(BaseModel):
    id: str
    name: str
    stops: List[str]
