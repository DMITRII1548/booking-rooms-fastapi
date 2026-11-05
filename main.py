from fastapi import FastAPI

from app.controllers.booking import router as booking_router
app = FastAPI()

app.include_router(booking_router, prefix="/bookings", tags=["booking"])