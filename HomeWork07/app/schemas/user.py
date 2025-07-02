from pydantic import (
    BaseModel,
    # EmailStr,
)


class UserBaseSchema(BaseModel):
    name: str
    username: str
    email: str | None = None
    phone: str | None = None
    website: str | None = None


class UserCreateSchema(UserBaseSchema):
    """
    Create User
    """


class UserReadSchema(UserBaseSchema):
    id: int
