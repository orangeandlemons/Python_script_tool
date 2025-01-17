import sqlite3


def connect_to_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor


def execute_query(cursor, query):
    cursor.execute(query)
    results = cursor.fetchall()
    return results


# 使用示例
conn, cursor = connect_to_database("/path/to/database.db")
query = "SELECT * FROM table_name"
results = execute_query(cursor, query)
print(results)
conn.close()
