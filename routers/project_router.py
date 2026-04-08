from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.project_service import ProjectService
from database.schemas.project_schema import ProjectCreate, ProjectRead, ProjectUpdate
from database.connection import get_db

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.create_project(
        name=project.name,
        description=project.description,
        start_date=project.start_date,
        places=[p.dict() for p in project.places]
    )


@router.get("/", response_model=list[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.list_projects()


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.get_project(project_id)


@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.update_project(
        project_id,
        name=project.name,
        description=project.description,
        start_date=project.start_date
    )


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.delete_project(project_id)
