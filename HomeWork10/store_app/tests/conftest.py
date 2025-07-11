import pytest
from ..models import Category, Product


@pytest.fixture
def category():
    return Category.objects.create(
        name="Тестовая категория",
        description="Тестовая категория",
    )


@pytest.fixture
def product(category):
    return Product.objects.create(
        name="Тестовый продукт",
        description="Тестовый продукт",
        price=10,
        category=category,
    )
