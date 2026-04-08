from sqlalchemy.orm import Session
from fastapi import HTTPException
from database.models.project import Project
from services.place_service import PlaceService

MAX_PLACES = 10


class ProjectService:
    def __init__(self, db: Session):
        self.db = db
        self.place_service = PlaceService(db)

    def list_projects(self):
        return self.db.query(Project).all()

    def get_project(self, project_id: int):
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project

    def create_project(self, name: str, description: str = None, start_date=None, places: list = []):
        if len(places) > MAX_PLACES:
            raise HTTPException(status_code=400, detail=f"Cannot add more than {MAX_PLACES} places")

        project = Project(name=name, description=description, start_date=start_date)
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        for place in places:
            self.place_service.add_place(project.id, place['external_id'], notes=place.get('notes'))

        return project

    def update_project(self, project_id: int, **kwargs):
        project = self.get_project(project_id)
        for key, value in kwargs.items():
            if hasattr(project, key) and value is not None:
                setattr(project, key, value)
        self.db.commit()
        self.db.refresh(project)
        return project

    def delete_project(self, project_id: int):
        project = self.get_project(project_id)
        if any(p.visited for p in project.places):
            raise HTTPException(status_code=400, detail="Cannot delete project with visited places")
        self.db.delete(project)
        self.db.commit()
        return {"detail": "Project deleted"}