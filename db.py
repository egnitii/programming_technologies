import os
import psycopg2
from psycopg2 import sql

# Пример использования подключения
if __name__ == "__main__":

    conn = psycopg2.connect(database="postgres", user="postgres", password="911911")
    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("Версия PostgreSQL:", version)

    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tables = cursor.fetchall()
    print("Таблицы в базе данных:")
    for table in tables:
       print(table[0])

    cursor.close()

    conn.close()