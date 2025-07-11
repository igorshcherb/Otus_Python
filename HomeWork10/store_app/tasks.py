from enum import StrEnum

from celery import shared_task


class ActionName(StrEnum):
    created = "Created"
    updated = "Updated"
    deleted = "Deleted"


@shared_task
def updated_product(product_name: str, action_name: ActionName) -> str:
    """
    Сообщение об изменении продукта

    :param action_name: Наименование изменения (created/updated/deleted)
    :param product_name: Наименование продукта
    """
    return f'{action_name} product "{product_name}"'
