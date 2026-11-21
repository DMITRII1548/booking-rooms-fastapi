from app.responses.booking import BookingWithUserResponse
from app.responses.room import DetailRoomResponse

# Resolve forward references between response modules (avoids circular imports)
DetailRoomResponse.model_rebuild(
    _types_namespace={"BookingWithUserResponse": BookingWithUserResponse}
)
