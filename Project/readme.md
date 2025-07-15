## <div align="center"> Проектная работа по курсу "Python Developer. Basic" <div align="center"> ##

# <div align="center"> Разработка системы анализа производительности </div> # 

# <div align="center"> СУБД и MPP-кластеров </div> #

**Цель проекта:**
Создание системы анализа производительности DBBS - DataBase Benchmark System

**Задачи проекта:**

1. Разработать БД для хранения запросов, групп, результатов выполнения
2. Создать утилиту для работы с системой DBBS через командную строку
3. На основе фреймворка Django создать приложение для администрирования DBBS
4. Обеспечить наглядное представление результатов проверки производительности
5. Выполнить замеры производительности нескольких СУБД и MPP-кластеров

[Презентация PDF](Презентация.pdf) [PPTX](Презентация.pptx)

**Команды в терминале**

```
cd Project\util
python dbbs_cli.py -b gr1 benchmark01
python dbbs_cli.py -r benchmark01
python dbbs_cli.py -h

cd Project

django-admin startproject dbbs_app
django-admin startproject config .

python manage.py runserver
python manage.py startapp dbbs_app
```
 