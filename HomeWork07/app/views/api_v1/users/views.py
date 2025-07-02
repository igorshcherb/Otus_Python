import sqlalchemy
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
)
from pydantic import PositiveInt

from async_requests import AsyncJsonplaceholderService
from config import BASE_API_URL
from models import User
from .crud import UserStorage

from schemas import (
    UserCreateSchema,
    UserReadSchema,
)

from .dependencies import (
    users_crud_dependency,
    get_user_by_filter,
)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/create-from-api/",
    status_code=status.HTTP_201_CREATED,
    response_model=list[UserReadSchema],
    description="Загрузить пользователей, полученных из api-ручки, в БД"
)
async def create_users_from_api(
    storage: UserStorage = Depends(users_crud_dependency),
) -> list[User]:
    client = AsyncJsonplaceholderService(base_url=BASE_API_URL)
    users_from_api = [UserCreateSchema(**x) for x in await client.fetch_users()]
    try:
        return await storage.create_users_from_api(
            users=[User(**x.model_dump()) for x in users_from_api],
        )
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Users from API had added already",
        )


@router.get(
    "/",
    response_model=list[UserReadSchema],
)
async def get_users_list(
    storage: UserStorage = Depends(users_crud_dependency),
) -> list[User]:
    return await storage.get()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserReadSchema,
)
async def create_user(
    user_in: UserCreateSchema,
    storage: UserStorage = Depends(users_crud_dependency),
) -> User:
    return await storage.create(user_in=user_in)


@router.get("/find/", response_model=UserReadSchema)
def get_by_filter(
    user: User = Depends(get_user_by_filter),
) -> User:
    return user


@router.get(
    "/{user_id}/",
    response_model=UserReadSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User #0 not found",
                    },
                },
            },
        },
    },
)
async def get_user(
    user_id: PositiveInt,
    storage: UserStorage = Depends(users_crud_dependency),
) -> User:
    user = await storage.get_by_id(user_id=user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
