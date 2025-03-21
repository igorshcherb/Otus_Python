class Contact:
    """
    Класс контакта
    """

    def __init__(self, name: str, phone: str, comment: str):
        """
        Инициализация экземпляра класса
        :param name: имя контакта
        :param phone: номер телефона
        :param comment: комментарий
        """
        self.name = name
        self.phone = phone
        self.comment = comment
