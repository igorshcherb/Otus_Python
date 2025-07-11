import pytest
from django.urls import reverse
from ..models import Product


# @pytest.mark.django_db
def test_index_view(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert "Главная" in response.content.decode("utf-8")
