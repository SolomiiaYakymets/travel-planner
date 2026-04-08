from typing import Optional
from .base_schema import BaseSchema


class PlaceCreate(BaseSchema):
    external_id: int
    notes: Optional[str] = None


class PlaceUpdate(BaseSchema):
    notes: Optional[str] = None
    visited: Optional[bool] = None


class PlaceRead(BaseSchema):
    id: int
    external_id: int
    name: str
    notes: Optional[str] = None
    visited: bool = False
