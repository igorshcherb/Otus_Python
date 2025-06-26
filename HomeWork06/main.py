import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from models import async_engine, User, Post, Base
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from typing import List, Dict
from sqlalchemy.orm import sessionmaker

async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def drop_create_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_users(session: AsyncSession, users_data: List[Dict]):
    users = [
        User(name=user["name"], username=user["username"], email=user["email"])
        for user in users_data
    ]
    session.add_all(users)
    await session.commit()
    return len(users)


async def add_posts(session: AsyncSession, posts_data: List[Dict]):
    posts = [
        Post(user_id=post["userId"], title=post["title"], body=post["body"])
        for post in posts_data
    ]
    session.add_all(posts)
    await session.commit()
    return len(posts)


async def async_main():
    await drop_create_db()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with async_session() as session:
        added_users = await add_users(session, users_data)
        added_posts = await add_posts(session, posts_data)


if __name__ == "__main__":
    asyncio.run(async_main())
