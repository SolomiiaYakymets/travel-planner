from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.place_service import PlaceService
from database.schemas.place_schema import PlaceCreate, PlaceRead, PlaceUpdate
from database.connection import get_db
from services.project_service import ProjectService

router = APIRouter(prefix="/places", tags=["places"])


@router.post("/projects/{project_id}", response_model=PlaceRead)
def add_place(project_id: int, place: PlaceCreate, db: Session = Depends(get_db)):
    service = PlaceService(db)
    return service.add_place(project_id, place.external_id, notes=place.notes)


@router.put("/{place_id}", response_model=PlaceRead)
def update_place(place_id: int, place: PlaceUpdate, db: Session = Depends(get_db)):
    service = PlaceService(db)
    return service.update_place(place_id, notes=place.notes, visited=place.visited)


@router.get("/{project_id}/places/", response_model=list[PlaceRead])
def list_places(project_id: int, db: Session = Depends(get_db)):
    project_service = ProjectService(db)
    project_service.get_project(project_id)

    place_service = PlaceService(db)
    return place_service.list_places_for_project(project_id)


@router.get("/{project_id}/places/{place_id}", response_model=PlaceRead)
def get_place(project_id: int, place_id: int, db: Session = Depends(get_db)):
    project_service = ProjectService(db)
    project_service.get_project(project_id)

    place_service = PlaceService(db)
    return place_service.get_place_in_project(project_id, place_id)
