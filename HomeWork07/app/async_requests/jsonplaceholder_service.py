"""
Асинхронные функции для выполнения запросов
"""

from .async_base import AsyncBase


class AsyncJsonplaceholderService(AsyncBase):
    async def fetch_users(self) -> list[dict]:
        """Получение списка"""
        return await self._get(url="users")

    async def fetch_user_by_id(self, user_id: int) -> dict:
        """
        Получение по id
        """
        return await self._get(f"users/{user_id}")
