import pytest
from ..models import Product, Category


@pytest.mark.django_db
def test_product_create(product):
    """Проверка создания продукта"""
    assert Product.objects.filter(id=product.pk).exists()
    assert product.name == "Тестовый продукт"
    assert product.description == "Тестовый продукт"
    assert product.price == 10


@pytest.mark.django_db
def test_product_delete(product):
    """Проверка удаления продукта"""
    assert Product.objects.filter(id=product.pk).exists()
    product.delete()
    assert not Product.objects.filter(id=product.pk).exists()


@pytest.mark.django_db
def test_product_update(product):
    """Проверка изменения продукта"""
    product.price = 20
    product.save()
    product_upd = Product.objects.get(pk=product.pk)
    assert product_upd.price == 20


@pytest.mark.django_db
def test_product_get(product):
    """Проверка чтения продукта"""
    product_retrieved = Product.objects.get(id=product.pk)
    assert product_retrieved.name == "Тестовый продукт"
