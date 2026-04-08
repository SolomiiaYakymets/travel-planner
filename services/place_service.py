from sqlalchemy.orm import Session
from fastapi import HTTPException
from database.models.project import Project
from database.models.project_place import ProjectPlace
from services.artic_api import validate_place

MAX_PLACES = 10


class PlaceService:
    def __init__(self, db: Session):
        self.db = db

    def add_place(self, project_id: int, external_id: int, notes: str = None):
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        if len(project.places) >= MAX_PLACES:
            raise HTTPException(status_code=400, detail=f"Cannot add more than {MAX_PLACES} places")

        if any(p.external_id == external_id for p in project.places):
            raise HTTPException(status_code=400, detail="Place already exists in project")

        valid, title = validate_place(external_id)
        if not valid:
            raise HTTPException(status_code=400, detail=f"Place {external_id} not found in Art Institute API")

        place = ProjectPlace(
            project_id=project_id,
            external_id=external_id,
            name=title,
            notes=notes,
            visited=False
        )
        self.db.add(place)
        self.db.commit()
        self.db.refresh(place)
        return place

    def update_place(self, place_id: int, notes: str = None, visited: bool = None):
        place = self.db.query(ProjectPlace).filter(ProjectPlace.id == place_id).first()
        if not place:
            raise HTTPException(status_code=404, detail="Place not found")

        if notes is not None:
            place.notes = notes
        if visited is not None:
            place.visited = visited

        self.db.commit()

        project = place.project
        if all(p.visited for p in project.places):
            project.completed = True
            self.db.commit()

        self.db.refresh(place)
        return place

    def list_places_for_project(self, project_id: int):
        places = self.db.query(ProjectPlace).filter_by(project_id=project_id).all()
        if not places:
            raise HTTPException(status_code=404, detail="No places found for this project")
        return places

    def get_place_in_project(self, project_id: int, place_id: int):
        place = (
            self.db.query(ProjectPlace)
            .filter_by(project_id=project_id, id=place_id)
            .first()
        )
        if not place:
            raise HTTPException(status_code=404, detail="Place not found in this project")
        return place
