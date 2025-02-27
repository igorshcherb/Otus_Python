file_name = "catalog.txt"
catalog = []
catalog_file = None

# Меню
print("1 - Открыть файл")
print("2 - Сохранить файл")
print("3 - Показать все контакты")
print("4 - Создать контакт")
print("5 - Найти контакт")
print("6 - Изменить контакт")
print("7 - Удалить контакт")
print("8 - Выход")

while True:
    input_dig = int(input("Введите цифру 1..8: "))
    if input_dig == 1:
        # Открытие файла
        catalog_file = open(file_name, "r", encoding="UTF-8")
        catalog = [item.strip().split(";") for item in catalog_file.readlines()]
        print("Файл открыт")
    elif input_dig == 2:
        # Сохранение файла
        if not catalog_file:
            print("Сначала откройте файл")
        else:
            catalog_tmp = ""
            for row in catalog:
                catalog_tmp = catalog_tmp + ";".join(row) + "\n"
            catalog_file.close()
            catalog_file = open(file_name, "w", encoding="UTF-8")
            catalog_file.write(catalog_tmp)
            catalog_file.close()
            print("Файл сохранен")
    elif input_dig == 3:
        # Показ всех контактов
        if not catalog_file:
            print("Сначала откройте файл")
        else:
            for cat_line in catalog:
                print(f"{cat_line[0]:<9} {cat_line[1]:<12} {cat_line[2]}")
    elif input_dig == 4:
        # Создание контакта
        if not catalog_file:
            print("Сначала откройте файл")
        else:
            new_name = input("Введите имя нового контакта: ")
            new_phone = input("Введите телефон: ")
            new_comment = input("Введите комментарий: ")
            catalog.append([new_name, new_phone, new_comment])
            print("Контакт создан")
    elif input_dig == 5:
        # Поиск контакта
        if not catalog_file:
            print("Сначала откройте файл")
        else:
            search_name = input("Введите имя для поиска: ")
            found = False
            for cat_line in catalog:
                if cat_line[0] == search_name:
                    print(f"{cat_line[0]:<9} {cat_line[1]:<12} {cat_line[2]}")
                    found = True
                    break
            if not found:
                print(search_name + " - не найдено.")
    elif input_dig == 6:
        # Изменение контакта
        if not catalog_file:
            print("Сначала откройте файл")
        else:
            change_name = input("Введите имя для изменения: ")
            found = False
            for cat_line in catalog:
                if cat_line[0] == change_name:
                    change_phone = input("Введите телефон: ")
                    change_comment = input("Введите комментарий: ")
                    cat_line[1] = change_phone
                    cat_line[2] = change_comment
                    found = True
                    break
            if not found:
                print(change_name + " - не найдено.")
            else:
                print("Контакт изменен")
    elif input_dig == 7:
        # Удаление контакта
        if not catalog_file:
            print("Сначала откройте файл")
        else:
            delete_name = input("Введите имя для удаления: ")
            found = False
            for cat_line in catalog:
                if cat_line[0] == delete_name:
                    catalog.remove(cat_line)
                    found = True
                    break
            if not found:
                print(delete_name + " - не найдено.")
            else:
                print("Контакт удален")
    elif input_dig == 8:
        # Выход
        break
    else:
        print("Неправильная цифра.")
