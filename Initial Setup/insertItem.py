import mysql.connector
import os
from dotenv import load_dotenv
import csv
import pandas as pd
import numpy as np

# This is a script for testing purposes only!!!

load_dotenv(override=True)

dbname = os.getenv('DB_DATABASE')
username = os.getenv('DB_USER')
passwd = os.getenv('DB_PASSWORD')
hostname = os.getenv('DB')
portnum = os.getenv('DB_PORT')


def connect():
    connection = mysql.connector.connect(
        database = dbname,
        user = username,
        password = passwd,
        host = hostname,
        port = portnum,
    )
    return connection

tableName = "item"

def generate_insert_sql(row):
    sql = f"INSERT IGNORE INTO {tableName} (ItemName) VALUES ("
    sql += f"'{row['Item']}'"
    sql += ");"
    return sql

def insert(sql, conn):
    with conn.cursor() as query:
            query.execute(sql)
    conn.commit()

def main():
    conn = connect()
    with open('./Initial Setup/ourItems.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Generate SQL insert statement for each row
            print(row)
            sql = generate_insert_sql(row)
            insert(sql, conn)


if __name__ == "__main__":
    main()
