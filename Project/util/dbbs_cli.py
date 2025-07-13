import psycopg2

filepath = "dbbs.ini"
delimiter = "="


def get_params_from_ini(p_filepath: str, p_delimiter: str) -> dict:
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
    v_cur = p_connection.cursor()
    v_cur.execute(
        f"select type_code, host, port, database, username, password from connections where code = '{p_code}'"
    )
    row1 = v_cur.fetchone()
    v_params = {
        "host": row1[0],
        "port": row1[1],
        "database": row1[2],
        "user": row1[3],
        "password": row1[4],
    }
    return v_params


dbbs_params: dict = get_params_from_ini(filepath, delimiter)
dbbs_conn = psycopg2.connect(
    host=dbbs_params.get("host"),
    port=dbbs_params.get("port"),
    database=dbbs_params.get("database"),
    user=dbbs_params.get("user"),
    password=dbbs_params.get("password"),
)
dbbs_cur = dbbs_conn.cursor()
dbbs_cur.execute("select code, description from connection_types")
rows = dbbs_cur.fetchall()
for row in rows:
    str1 = row[0] + " | " + row[1]
    print(str1)

test_db_params = get_params_from_db(dbbs_conn, "pg1")

print(test_db_params)

# cur.execute("select * from connections")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
