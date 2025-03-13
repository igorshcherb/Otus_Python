from view import *
from model import Contact, Catalog

catalog = Catalog()


def file_opened() -> bool:
    if not catalog.get_catalog_file():
        alert_open_file()
        ret_value = False
    else:
        ret_value = True
    return ret_value


def start_app():
    """
    Запуск приложения
    """
    print_menu()
    finish = False
    while not finish:
        input_dig = get_digit()
        if input_dig == 1:
            # Открытие файла
            catalog.open_file()
            info_file_opened()
        elif input_dig == 2:
            # Сохранение файла
            if file_opened():
                catalog.save_file()
                info_file_saved()
        elif input_dig == 3:
            # Показ всех контактов
            if file_opened():
                print_catalog(catalog.get_catalog_list())
        elif input_dig == 4:
            # Создание контакта
            if file_opened():
                contact_list = get_new_contact_data()
                contact = Contact(contact_list[0], contact_list[1], contact_list[2])
                catalog.append_contact(contact)
                info_contact_created()
        elif input_dig == 5:
            # Поиск контакта
            if file_opened():
                search_name = get_name_to_search()
                output_str(catalog.search_contact(search_name))
        elif input_dig == 6:
            # Изменение контакта
            if file_opened():
                change_data = get_data_to_change()
                contact = Contact(change_data[0], change_data[1], change_data[2])
                output_str(catalog.update_contact(contact))
        elif input_dig == 7:
            # Удаление контакта
            if file_opened():
                delete_name = get_name_to_delete()
                output_str(catalog.delete_contact(delete_name))
        elif input_dig == 8:
            # Выход
            finish = True
        else:
            # Неправильная цифра
            alert_wrong_digit()


if __name__ == "__main__":
    start_app()
