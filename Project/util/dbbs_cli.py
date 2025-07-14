import sys
import psycopg2
from datetime import datetime

filepath = "dbbs.ini"
delimiter = "="
execution_time = "Execution Time: "


def get_params_from_ini(p_filepath: str, p_delimiter: str) -> dict:
    """
    Получение из файла ini параметров для соединения со служебной БД
    """
    v_params = {}
    try:
        with open(p_filepath, "r") as file:
            for line in file:
                line = line.strip()
                if line and p_delimiter in line:
                    key, value = line.split(p_delimiter, 1)
                    v_params[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден {p_filepath}")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return v_params


def get_params_from_db(p_connection, p_code: str) -> dict:
    """
    Получение параметров для соединения с БД, в которой требуется провести тесты производительности
    """
    v_cur = p_connection.cursor()
    v_cur.execute(
        f"select type_code, host, port, database, username, password from connections where code = '{p_code}'"
    )
    row1 = v_cur.fetchone()
    v_params = {
        "host": row1[1],
        "port": row1[2],
        "database": row1[3],
        "user": row1[5],
        "password": row1[5],
    }
    return v_params


# получение группы запросов из командной строки
group_code = sys.argv[1]

# получение параметров и соединение со служебной БД
dbbs_params: dict = get_params_from_ini(filepath, delimiter)
dbbs_conn = psycopg2.connect(
    host=dbbs_params.get("host"),
    port=dbbs_params.get("port"),
    database=dbbs_params.get("database"),
    user=dbbs_params.get("user"),
    password=dbbs_params.get("password"),
)

# открытие курсора в служебной БД
dbbs_cur = dbbs_conn.cursor()

# соединение с тестовой БД
test_db_params = get_params_from_db(dbbs_conn, "pg1")
test_conn = psycopg2.connect(
    host=test_db_params.get("host"),
    port=test_db_params.get("port"),
    database=test_db_params.get("database"),
    user=test_db_params.get("user"),
    password=test_db_params.get("password"),
)
test_cur = test_conn.cursor()
# установка схемы в тестовой БД
test_cur.execute("set schema 'bookings'")

# запись в БД имени теста и времени начала
current_datetime = datetime.now()
str0 = "benchmark " + str(current_datetime)
str1 = f"insert into benchmarks(name, start_datetime) values('{str0}','{current_datetime}'::timestamp) returning id"
dbbs_cur.execute(str1)
dbbs_row = dbbs_cur.fetchone()
benchmark_id = "".join(str(x) for x in dbbs_row)
str1 = "commit"
dbbs_cur.execute(str1)

# получение запросов заданной группы из служебной БД
str0 = f"""select q.code, q.query_text
    from queries_in_groups qin
     left join queries q on q.code = qin.query_code
    where qin.group_code = '{group_code}'"""
dbbs_cur.execute(str0)

# открытие второго курсов в служебной БД - для записи результатов тестирования
dbbs_cur_2 = dbbs_conn.cursor()

dbbs_rows = dbbs_cur.fetchall()
for dbbs_row in dbbs_rows:
    str1 = "explain analyze " + dbbs_row[1]
    test_cur.execute(str1)
    test_rows = test_cur.fetchall()
    for test_row in test_rows:
        result_str = "".join(str(x) for x in test_row)
        if execution_time in result_str:
            execution_time_pos = result_str.find(execution_time) + len(execution_time)
            space_pos = result_str.find(" ", execution_time_pos)
            time_value = result_str[execution_time_pos:space_pos]
            try:
                time_float = float(time_value)
            except ValueError:
                print(f"Ошибка преобразования '{time_value}' в число.")
            # запись в таблицу результата
            current_datetime = datetime.now()
            command_str = f"""insert into benchmark_items(benchmark_id, query_code, start_datetime, result)
                values({benchmark_id}, '{dbbs_row[0]}', '{current_datetime}'::timestamp, {time_value})"""
            dbbs_cur_2.execute(command_str)
        command_str = "commit"
        dbbs_cur_2.execute(command_str)
    print(f"Запрос: {dbbs_row[0]}")
# закрытие курсоров
test_cur.close()
dbbs_cur_2.close()
dbbs_cur.close()
