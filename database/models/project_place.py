from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.models.core import Base


class ProjectPlace(Base):
    __tablename__ = "project_places"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    external_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    visited = Column(Boolean, default=False)

    project = relationship("Project", back_populates="places")
