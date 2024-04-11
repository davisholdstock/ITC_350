import mysql.connector
import os
from dotenv import load_dotenv
import csv
import pandas as pd
import numpy as np

# This is a script for testing purposes only!!!

load_dotenv(override=True)

dbname = os.getenv('DB_NAME')
username = os.getenv('DB_USER')
passwd = os.getenv('DB_PASSWORD')
hostname = os.getenv('DB_HOST')
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

tableName = "recipe"

def generate_insert_sql(row):
    directions = row['Directions'].replace("$", ",")
    directions = directions.replace(";", ",")
    sql = f"INSERT INTO {tableName} (Rating, Difficulty, Directions, Duration, Title, Category, Picture) VALUES ("
    sql += f"{row['Rating']}, {row['Difficulty']}, '{directions}', {row['Duration']}, '{row['Title']}', '{row['Category']}', '{row['Picture']}'"
    sql += ");"
    return sql

def insert(sql, conn):
    with conn.cursor() as query:
            query.execute(sql)
    conn.commit()

def main():
    conn = connect()
    with open('ITC_350/Initial Setup/ourRecipies.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Generate SQL insert statement for each row
            print(row)
            sql = generate_insert_sql(row)
            insert(sql, conn)


if __name__ == "__main__":
    main()
