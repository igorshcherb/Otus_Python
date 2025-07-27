## <div align="center"> Проектная работа по курсу "Python Developer. Basic" <div align="center"> ##

# <div align="center"> Разработка системы анализа производительности </div> # 

# <div align="center"> СУБД и MPP-кластеров </div> #

**Цель проекта:**
Создание системы анализа производительности запросов DBBS - Data Base Benchmark System

**Задачи проекта:**

1. Разработать вспомогательную БД для хранения запросов, групп, результатов выполнения запросов.
2. Создать утилиту для работы с системой DBBS через командную строку.
3. На основе фреймворка Django создать приложение для администрирования DBBS.
4. Обеспечить представление замеров производительности.
5. Выполнить замеры производительности.

**Презентация:** [PDF](results/Presentation.pdf) [PPTX](results/Presentation.pptx)

**Вспомогательная БД**

[Диаграмма](results/DB_diagram.jpg)

[Скрипты БД](SQL/)

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

**Результаты замеров производительности**

[Postgres № 1](results/benchmarks/benchmark_pg1_01.txt)   
[Postgres № 2](results/benchmarks/benchmark_pg1_02.txt)   
[Сравнение замеров Postgres](results/benchmarks/compare_pg1_01_02.txt)   
[ArenadataDB № 1](results/benchmarks/benchmark_adb_01.txt)   
[ArenadataDB № 2](results/benchmarks/benchmark_adb_02.txt)   
[Сравнение замеров ArenadataDB](results/benchmarks/compare_adb_01_02.txt)   
   