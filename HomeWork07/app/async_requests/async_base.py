import asyncio

import aiohttp


class AsyncBase:

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def _get(self, url: str, timeout: int = 1) -> dict:
        """
        Базовая функция для GET-запроса
        """
        async with asyncio.timeout(timeout):
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/{url}") as response:
                    response.raise_for_status()
                    return await response.json()

    async def _delete(self, url: str, timeout: int = 0.5) -> dict:
        """
        Базовая функция для DELETE-запросов
        """
        async with asyncio.timeout(timeout):
            async with aiohttp.ClientSession() as session:
                async with session.delete(f"{self.base_url}/{url}") as response:
                    response.raise_for_status()
                    return await response.json()

    async def _post(self, url: str, data: dict, timeout: int = 0.5) -> dict:
        """
        Базовая функция для POST-запросов
        """
        async with asyncio.timeout(timeout):
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/{url}", data=data
                ) as response:
                    response.raise_for_status()
                    return await response.json()

    async def _put(self, url: str, data: dict, timeout: int = 0.5) -> dict:
        """
        Базовая функция для PUT-запросов
        """
        async with asyncio.timeout(timeout):
            async with aiohttp.ClientSession() as session:
                async with session.put(f"{self.base_url}/{url}", data=data) as response:
                    response.raise_for_status()
                    return await response.json()

    async def _patch(self, url: str, data: dict, timeout: int = 0.5) -> dict:
        """
        Базовая функция для PATCH-запросов
        """
        async with asyncio.timeout(timeout):
            async with aiohttp.ClientSession() as session:
                async with session.patch(
                    f"{self.base_url}/{url}", data=data
                ) as response:
                    response.raise_for_status()
                    return await response.json()
