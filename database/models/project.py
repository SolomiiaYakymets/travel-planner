from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from database.models.core import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
    completed = Column(Boolean, default=False)

    places = relationship("ProjectPlace", back_populates="project", cascade="all, delete-orphan")
