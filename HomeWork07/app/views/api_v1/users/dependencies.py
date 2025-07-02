from collections.abc import AsyncGenerator

from fastapi import Depends, HTTPException, status
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.engine import async_session
from .crud import UserStorage


async def async_session_dependency() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session


"""
Связь между AuthorStorage и async сессией
(чтобы AuthorStorage не был завязан на веб, а только на модельки и схемы)
"""
def users_crud_dependency(
    session: AsyncSession = Depends(async_session_dependency),
) -> UserStorage:
    return UserStorage(session=session)


async def get_user_by_filter(
    email: EmailStr | None = None,
    name: str | None = None,
    username: str | None = None,
    storage: UserStorage = Depends(users_crud_dependency),
) -> User:
    if email:
        user = await storage.get_by_filter(email=email)
    else:
        user = await storage.get_by_filter(username=username)

    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author by {email=} not found",
    )
