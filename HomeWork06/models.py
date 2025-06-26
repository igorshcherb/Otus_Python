from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    Mapped,
    mapped_column,
    relationship,
)


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@192.168.2.171/db01"

async_engine = create_async_engine(DATABASE_URL, echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        unique=True,
    )
    username: Mapped[str] = mapped_column(
        String(length=32),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        String(length=150),
        unique=True,
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(120),
        index=True,
        default="",
        server_default="",
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )
