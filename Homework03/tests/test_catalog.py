from Homework03.catalog import Catalog
from Homework03.contact import Contact


class TestCatalog:
    def test_append_contact(self):
        """
        Тест добавления контакта
        """
        catalog = Catalog()
        contact = Contact('AAA', '111', 'comment')
        catalog.append_contact(contact)

    def test_search_contact(self):
        """
        Тест поиска контакта
        """
        pass

    def test_update_contact(self):
        """
        Тест изменения контакта
        """
        pass

    def test_delete_contact(self):
        """
        Тест удаления контакта
        """
        pass

    def test_open_file(self):
        """
        Тест открытия файла
        """
        pass

    def test_save_file(self):
        """
        Тест сохранения файла
        """
        pass
