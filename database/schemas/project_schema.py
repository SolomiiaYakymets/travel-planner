from typing import Optional, List
from datetime import date
from .base_schema import BaseSchema
from .place_schema import PlaceRead


class ProjectCreate(BaseSchema):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    places: Optional[List[PlaceRead]] = []


class ProjectUpdate(BaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None


class ProjectRead(BaseSchema):
    id: int
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    completed: bool = False
    places: List[PlaceRead] = []
