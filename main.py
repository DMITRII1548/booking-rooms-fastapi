from contextlib import asynccontextmanager

from fastapi import FastAPI

import app.models  # noqa: F401  registers models in Base.metadata
from app.controllers.booking import router as booking_router
from app.database import Base, SessionLocal, engine
from app.seed import seed


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed(db)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(booking_router, prefix="/bookings", tags=["booking"])
