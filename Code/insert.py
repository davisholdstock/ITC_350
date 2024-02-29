import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(override=True)

dbname = os.getenv('databasename')
username = os.getenv('username')
passwd = os.getenv('password')
hostname = os.getenv('host')
portnum = os.getenv('port')

def connect():
    connection = mysql.connector.connect(
        database = dbname,
        user = username,
        password = passwd,
        host = hostname,
        port = portnum,
    )
    return connection


def create_table(connection):
    with connection.cursor() as query:
        query.execute("""
            CREATE TABLE IF NOT EXISTS test (
                id INT AUTO_INCREMENT PRIMARY KEY,
                test VARCHAR(255)
            )
            """)
    connection.commit()

def insert_data(connection):
    with connection.cursor() as query:
        query.execute("""
            INSERT INTO test (test) VALUES ('test');
""")
    connection.commit()

def delete_data(connection):
    with connection.cursor() as query:
        query.execute("""
            DELETE FROM test WHERE id=2;
""")
    connection.commit()


def main():
    create_table(connect())
    insert_data(connect())
    delete_data(connect())

if __name__ == "__main__":
    main()
