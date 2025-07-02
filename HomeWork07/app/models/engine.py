import config


"""Асинхронный движок БД"""
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)


# движок
async_engine = create_async_engine(
    url=config.PG_CONN_URI,
    echo=config.SQLALCHEMY_ECHO,
    pool_size=config.SQLALCHEMY_POOL_SIZE,
    max_overflow=config.SQLALCHEMY_MAX_OVERFLOW,
)

# сессия
async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
)
