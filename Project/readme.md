## <div align="center"> Проектная работа по курсу "Python Developer. Basic" <div align="center"> ##

# <div align="center"> Разработка системы анализа производительности </div> # 

# <div align="center"> СУБД и MPP-кластеров </div> #

**Цель проекта:**
Создание системы анализа производительности DBBS - DataBase Benchmark System

**Задачи проекта:**

1. Разработать БД для хранения запросов, групп, результатов выполнения тестов
2. Создать утилиту для работы с системой DBBS через командную строку
3. На основе фреймворка Django создать приложение для администрирования DBBS
4. Обеспечить наглядное представление результатов тестов производительности
5. Выполнить замеры производительности СУБД и MPP-кластера

[Презентация PDF](Презентация.pdf) [PPTX](Презентация.pptx)

**Команды в терминале для работы с утилитой командной строки**

``` 
cd Project\util
python dbbs_cli.py -b gr1 benchmark01 pg1
python dbbs_cli.py -r benchmark01
python dbbs_cli.py -c benchmark01 benchmark02
python dbbs_cli.py -h
```

**Команды в терминале для создания приложения Django**

```
cd Project
django-admin startproject config .
python manage.py startapp dbbs_app
```

**Команды в терминале для работы с приложением Django**

```
cd Project
python manage.py runserver
```
