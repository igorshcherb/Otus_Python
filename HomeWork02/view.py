def print_menu() -> None:
    """
    Вывод меню в консоль
    """
    print("1 - Открыть файл")
    print("2 - Сохранить файл")
    print("3 - Показать все контакты")
    print("4 - Создать контакт")
    print("5 - Найти контакт")
    print("6 - Изменить контакт")
    print("7 - Удалить контакт")
    print("8 - Выход")


def alert_open_file() -> None:
    """
    Предупреждение: необходимо открыть файл
    """
    print("Сначала откройте файл")


def info_file_opened() -> None:
    """
    Сообщение: Файл открыт
    """
    print("Файл открыт")


def info_file_saved() -> None:
    """
    Сообщение: Файл сохранен
    """
    print("Файл сохранен")


def info_contact_created() -> None:
    """
    Сообщение: Контакт создан
    """
    print("Контакт создан")


def get_new_contact_data() -> (str, str, str):
    """
    Получение от пользователя данных нового контакта
    :return: str, str, str
    """
    new_name = input("Введите имя нового контакта: ")
    new_phone = input("Введите телефон: ")
    new_comment = input("Введите комментарий: ")
    return new_name, new_phone, new_comment


def get_name_to_search() -> str:
    """
    Получение от пользователя имени для поиска
    :return: str
    """
    search_name = input("Введите имя для поиска: ")
    return search_name


def get_data_to_change() -> (str, str, str):
    """
    Получение от пользователя данных для изменения
    :return: (str, str, str)
    """
    change_name = input("Введите имя для изменения: ")
    change_phone = input("Введите телефон: ")
    change_comment = input("Введите комментарий: ")
    return change_name, change_phone, change_comment


def get_name_to_delete() -> str:
    """
    Получение от пользователя имени для удаления
    :return: str
    """
    delete_name = input("Введите имя для удаления: ")
    return delete_name


def get_digit() -> int:
    """
    Получение от пользователя цифры, соответствующей пункту меню
    :return: int
    """
    input_dig = int(input("Введите цифру 1..8: "))
    return input_dig


def alert_wrong_digit() -> None:
    """
    Предупреждение: введена неправильная цифра
    """
    print("Неправильная цифра.")


def print_catalog(catalog_list: list) -> None:
    """
    Показ всех контактов
    """
    for cat_line in catalog_list:
        print(f"{cat_line[0]:<9} {cat_line[1]:<12} {cat_line[2]}")


def output_str(out_str: str):
    print(out_str)


if __name__ == "__main__":
    print(get_new_contact_data())
