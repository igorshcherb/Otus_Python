FROM python:3.11


# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTTRIGGERBYCODE=1


# Устанавливаем рабочую директорию
WORKDIR /var/app

# Установка poetry
RUN pip install --upgrade pip wheel poetry
RUN poetry config virtualenvs.create false


# Копируем файлы зависимостей
COPY poetry.lock pyproject.toml ./


# Устанавливаем зависимости
RUN poetry install


# Копируем остальную часть приложения
COPY app .

RUN chmod +x prestart.sh
