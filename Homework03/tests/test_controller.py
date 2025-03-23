import sys

sys.path.append("./Homework03")
from controller import file_opened
from catalog import Catalog


class TestController:
    def test_file_opened(self) -> None:
        """
        Проверка функции file_opened()
        """
        catalog = Catalog()
        opened = file_opened(catalog)
        assert opened == False
        catalog.open_file()
        opened = file_opened(catalog)
        assert True == opened
        catalog.close_file(catalog.get_catalog_file())
