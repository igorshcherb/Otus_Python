from io import TextIOWrapper

FILE_NAME = "catalog.txt"


class Contact:
    """
    Класс контакта
    """

    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment


class Catalog:
    """
    Класс каталога
    """

    def __init__(self):
        self.__catalog_list = None
        self.__catalog_file = None

    def get_catalog_list(self) -> list:
        return self.__catalog_list

    def get_catalog_file(self) -> list:
        return self.__catalog_file

    def open_file(self) -> None:
        self.__catalog_file = open(FILE_NAME, "r", encoding="UTF-8")
        self.__catalog_list = [
            item.strip().split(";") for item in self.__catalog_file.readlines()
        ]

    def save_file(self) -> None:
        catalog_tmp = ""
        for row in self.__catalog_list:
            catalog_tmp = catalog_tmp + ";".join(row) + "\n"
        self.__catalog_file.close()
        catalog_file = open(FILE_NAME, "w", encoding="UTF-8")
        catalog_file.write(catalog_tmp)
        catalog_file.close()

    def append_contact(self, contact: Contact) -> None:
        self.__catalog_list.append([contact.name, contact.phone, contact.comment])

    def search_contact(self, search_name: str) -> str:
        ret_value = None
        found = False
        for cat_line in self.__catalog_list:
            if cat_line[0] == search_name:
                ret_value = f"{cat_line[0]:<9} {cat_line[1]:<12} {cat_line[2]}"
                found = True
                break
        if not ret_value:
            ret_value = search_name + " - не найдено."
        return ret_value

    def update_contact(self, contact: Contact) -> str:
        found = False
        for cat_line in self.__catalog_list:
            if cat_line[0] == contact.name:
                cat_line[1] = contact.phone
                cat_line[2] = contact.comment
                found = True
                ret_value = "Контакт изменен"
                break
        if not found:
            ret_value = contact.name + " - не найдено."
        return ret_value

    def delete_contact(self, delete_name: str) -> str:
        found = False
        for cat_line in self.__catalog_list:
            if cat_line[0] == delete_name:
                self.__catalog_list.remove(cat_line)
                found = True
                ret_value = "Контакт удален"
                break
        if not found:
            ret_value = delete_name + " - не найдено."
        return ret_value
