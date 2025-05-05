from io import TextIOWrapper
from typing import TextIO
from contact import Contact
from pathlib import Path

# Имя файла каталога
FILE_NAME: str = "catalog.txt"
NOT_FOUND: str = " - не найдено."
TESTS_DIR: str = "tests"
HOMEWORK_DIR: str = "HomeWork03"


class Catalog:
    """
    Класс каталога
    """

    def __init__(self):
        """
        Инициализация экземпляра класса
        """
        self.__catalog_list = None
        self.__catalog_file = None

    def get_catalog_list(self) -> list:
        """
        Получение атрибута: __catalog_list
        :return: список справочника
        """
        return self.__catalog_list

    def get_catalog_file(self) -> TextIOWrapper:
        """
        Получение атрибута: __catalog_file
        :return: список справочника
        """
        return self.__catalog_file

    @staticmethod
    def get_current_filename() -> str:
        path = Path.cwd()
        if TESTS_DIR in str(path):
            path = path.parent
        if not HOMEWORK_DIR in str(path):
            path = path / HOMEWORK_DIR
        ret = str(path / FILE_NAME)
        return ret

    @staticmethod
    def open_file_to_read(file_name: str) -> TextIO:
        """
        Открытие файла на чтение
        """
        file_read = open(file_name, "r", encoding="UTF-8")
        return file_read

    def open_file(self) -> None:
        """
        Открытие файла справочника
        """
        self.__catalog_file = self.open_file_to_read(self.get_current_filename())
        self.__catalog_list = [
            item.strip().split(";") for item in self.__catalog_file.readlines()
        ]

    @staticmethod
    def close_file(current_file: TextIO) -> None:
        """
        Закрытие файла
        :rtype: object
        """
        current_file.close()

    def save_file(self) -> None:
        """
        Сохранение файла справочника
        """
        catalog_tmp = ""
        for row in self.__catalog_list:
            catalog_tmp = catalog_tmp + ";".join(row) + "\n"
        self.__catalog_file.close()
        self.close_file(self.get_catalog_file())
        catalog_file = open(self.get_current_filename(), "w", encoding="UTF-8")
        catalog_file.write(catalog_tmp)
        self.close_file(catalog_file)

    def append_contact(self, contact: Contact) -> None:
        """
        Добавление контакта в список справочника
        """
        self.__catalog_list.append([contact.name, contact.phone, contact.comment])

    @staticmethod
    def get_not_found() -> str:
        return NOT_FOUND

    def search_contact(self, search_name: str) -> str:
        """
        Поиск контакта в списке справочника
        :return: результат поиска
        """
        ret_value = None
        for cat_line in self.__catalog_list:
            if cat_line[0] == search_name:
                ret_value = f"{cat_line[0]:<9} {cat_line[1]:<12} {cat_line[2]}"
                break
        if not ret_value:
            ret_value = search_name + self.get_not_found()
        return ret_value

    def update_contact(self, contact: Contact) -> str:
        """
        Изменение контакта в списке справочника
        :return: результат изменения
        """
        found = False
        ret_value = ""
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
        """
        Удаление контакта из списка справочника
        :return: результат удаления
        """
        found = False
        ret_value = ""
        for cat_line in self.__catalog_list:
            if cat_line[0] == delete_name:
                self.__catalog_list.remove(cat_line)
                found = True
                ret_value = "Контакт удален"
                break
        if not found:
            ret_value = delete_name + " - не найдено."
        return ret_value
