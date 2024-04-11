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

tableName = "ingredient"

def generate_insert_sql(row):
    sql = f"INSERT IGNORE INTO {tableName} (Count, Units, IRecipeID, I_ItemID) VALUES ("
    sql += f"{row['Count']}, '{row['Units']}', (SELECT RecipeID as IRecipeID FROM recipe WHERE Title = '{row['Recipe Title']}'), (SELECT ItemID as I_ITEMID FROM Item WHERE ItemName = '{row['Item Name']}')"
    sql += ");"
    return sql

def insert(sql, conn):
    with conn.cursor() as query:
            query.execute(sql)
    conn.commit()

def main():
    conn = connect()
    with open('ourIngredients.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Generate SQL insert statement for each row
            print(row)
            sql = generate_insert_sql(row)
            insert(sql, conn)


if __name__ == "__main__":
    main()
