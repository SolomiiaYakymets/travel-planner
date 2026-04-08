from contextlib import asynccontextmanager

from fastapi import FastAPI

from database.connection import engine
from database.models.core import Base
import database.models.project
import database.models.project_place
from routers import project_router, place_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Travel Planner API",
    lifespan=lifespan
)

app.include_router(project_router.router)
app.include_router(place_router.router)
