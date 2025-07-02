"""
Create
Read
Update
Delete
"""
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User

from schemas import (
    UserCreateSchema,
)


class UserStorage:
    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self.session = session

    async def create(self, user_in: UserCreateSchema) -> User:
        """Создание пользователя"""
        user = User(
            **user_in.model_dump(),
        )
        self.session.add(user)
        await self.session.commit()
        return user

    async def create_users_from_api(self, users: list[User]) -> list[User]:
        """Создание авторов, полученных из api"""
        self.session.add_all(users)
        await self.session.commit()
        return users

    async def get(self) -> list[User]:
        """Получить список всех авторов"""
        stmt = select(User).order_by(User.id)
        results = await self.session.scalars(stmt)
        return list(results.all())

    async def get_by_id(self, user_id: int) -> User | None:
        """Получить пользователя по id"""
        return await self.session.get(User, user_id)

    async def get_by_filter(
        self,
        name: str | None = None,
        email: str | None = None,
        username: str | None = None,
    ) -> User | None:
        """Получить пользователя по email"""
        if name:
            stmt = select(User).where(User.name == name)
        elif username:
            stmt = select(User).where(User.username == username)
        else:
            stmt = select(User).where(User.email == email)
        return await self.session.scalar(stmt)
