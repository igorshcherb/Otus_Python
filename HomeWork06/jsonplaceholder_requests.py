import aiohttp
import asyncio
from typing import List, Dict
import logging
from common import configure_logging


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"

POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

log = logging.getLogger(__name__)


async def fetch_json(session: aiohttp.ClientSession, url: str) -> List[dict]:
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def fetch_users_data() -> List[dict]:
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, USERS_DATA_URL)


async def fetch_posts_data() -> List[dict]:
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, POSTS_DATA_URL)


async def async_main():
    configure_logging()
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    log.info(users_data)
    log.info(posts_data)


if __name__ == "__main__":
    asyncio.run(async_main())
