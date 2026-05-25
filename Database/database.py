import sqlite3
import csv

# DB connection
file_path = r"c:\Users\User\Desktop\python BI Rabindra sir\chinook.db"
conn = sqlite3.connect(file_path)
cursor = conn.cursor()

# Queries
sql = """
SELECT * FROM albums;
"""
cursor.execute(sql)
results=cursor.fetchall()
print(results)

# Add record in SQL via python
# csv_file_path = r"c:\Users\User\Desktop\python BI Rabindra sir\files\2022-01-02.csv"
# with open(csv_file_path, "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     data = list(reader)
# print(data)
# for row in data:
#     print(row)

# Creating table
# create_sql = """CREATE TABLE IF not EXISTS share_data(
# SNo varchar(255),
# Symbol varchar(255),
# Conf varchar(255),
# Open varchar(255)
# );
# """
# cursor.execute(create_sql)

# insert_sql = """
# INSERT INTO share_data(SNo, Symbol, Conf, Open)
# VALUES(?, ?, ?, ?);
# """
# cursor.executemany(insert_sql, data[1:])
# conn.commit()
