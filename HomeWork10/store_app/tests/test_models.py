import pytest
from ..models import Product


@pytest.mark.django_db
def test_product_create(product):
    """Проверка создания продукта"""
    assert Product.objects.count() == 1
    assert product.name == "Тестовый продукт"
    assert product.description == "Тестовый продукт"
    assert product.price == 10
