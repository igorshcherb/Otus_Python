from fastapi import APIRouter

from .users import router as users_router



api_v1 = APIRouter(
    prefix="/v1",
    tags=["API V1"],
)
api_v1.include_router(users_router)

