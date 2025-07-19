from celery import shared_task

@shared_task
def add_product_logging(name: str):
    print(f"Товар {name} успешно добавлен.")

