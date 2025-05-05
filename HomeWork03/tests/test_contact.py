import sys

sys.path.append("./HomeWork03")
import pytest
from contact import Contact


class TestContact:
    @pytest.mark.parametrize(
        "name, phone, comment",
        [
            ("a", "1", "c"),
            ("bb", "11", "cc"),
            (None, "11", "cc"),
        ],
    )
    def test_init(self, name: str, phone: str, comment: str):
        """
        Проверка порядка атрибутов
        """
        contact = Contact(name, phone, comment)
        assert name == contact.name
        assert phone == contact.phone
        assert comment == contact.comment
