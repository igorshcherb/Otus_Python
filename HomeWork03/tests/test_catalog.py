import sys

sys.path.append("./HomeWork03")
from catalog import Catalog
from contact import Contact


class TestCatalog:
    def test_append_contact(self):
        """
        Тест добавления контакта
        """
        catalog = Catalog()
        catalog.open_file()
        contact = Contact("AAA", "111", "comment")
        catalog.append_contact(contact)
        found = False
        for cat_line in catalog.get_catalog_list():
            if (
                    cat_line[0] == contact.name
                    and cat_line[1] == contact.phone
                    and cat_line[2] == contact.comment
            ):
                found = True
                break
        catalog.close_file(catalog.get_catalog_file())
        catalog = None
        contact = None

        assert found == True

    def test_search_contact(self):
        """
        Тест поиска контакта
        """
        catalog = Catalog()
        catalog.open_file()
        contact = Contact("AAA", "111", "comment")
        catalog.append_contact(contact)
        search_res = catalog.search_contact(contact.name)
        notfound = catalog.get_not_found() in search_res
        catalog.close_file(catalog.get_catalog_file())
        catalog = None
        contact = None
        assert notfound == False

    def test_update_contact(self):
        """
        Тест изменения контакта
        """
        catalog = Catalog()
        catalog.open_file()
        contact = Contact("AAA", "111", "comment")
        catalog.append_contact(contact)
        upd_contact = Contact(contact.name, contact.phone * 2, contact.comment * 2)
        catalog.update_contact(upd_contact)
        found = False
        for cat_line in catalog.get_catalog_list():
            if (
                    cat_line[0] == upd_contact.name
                    and cat_line[1] == upd_contact.phone
                    and cat_line[2] == upd_contact.comment
            ):
                found = True
                break
        catalog.close_file(catalog.get_catalog_file())
        catalog = None
        contact = None
        assert found == True

    def test_delete_contact(self):
        """
        Тест удаления контакта
        """
        catalog = Catalog()
        catalog.open_file()
        contact = Contact("AAA", "111", "comment")
        catalog.append_contact(contact)
        catalog.delete_contact(contact.name)
        found = False
        for cat_line in catalog.get_catalog_list():
            if (
                    cat_line[0] == contact.name
                    and cat_line[1] == contact.phone
                    and cat_line[2] == contact.comment
            ):
                found = True
                break
        catalog.close_file(catalog.get_catalog_file())
        catalog = None
        contact = None
        assert found == False

    def test_open_file(self):
        """
        Тест открытия файла
        """
        catalog = Catalog()
        catalog.open_file()
        opened = True
        if not catalog.get_catalog_file():
            opened = False
        catalog = None
        assert opened == True

    def test_save_file(self):
        """
        Тест сохранения файла
        """
        catalog = Catalog()
        catalog.open_file()
        contact = Contact("AAA", "111", "comment")
        catalog.append_contact(contact)
        catalog.save_file()
        catalog.close_file(catalog.get_catalog_file())
        catalog = None
        catalog = Catalog()
        catalog.open_file()
        found = False
        for cat_line in catalog.get_catalog_list():
            if (
                    cat_line[0] == contact.name
                    and cat_line[1] == contact.phone
                    and cat_line[2] == contact.comment
            ):
                found = True
                break
        catalog.delete_contact(contact.name)
        catalog.save_file()
        catalog.close_file(catalog.get_catalog_file())
        catalog = None
        assert found == True
