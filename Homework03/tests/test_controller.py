from Homework03.controller import file_opened
from Homework03.catalog import Catalog


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
        assert opened == True
        catalog.close_file(catalog.get_catalog_file())
