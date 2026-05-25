import sqlite3
import csv
import os
from mailerpy import Mailer

# Connect database
db_path = r"c:\Users\User\Desktop\python BI Rabindra sir\files\chinook.db"
csv_path = r"C:\Users\User\Desktop\python BI Rabindra sir\files\albums_report.csv"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch Data
sql = """SELECT * FROM albums LIMIT 10;"""
cursor.execute(sql)
rows = cursor.fetchall()
print(list(rows))

# Get column names
columns = [desc[0] for desc in cursor.description]
conn.close()

# CREATE csv file
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(rows)
print("CSV file created successfully.")

# Send Email
password= os.getenv("eike uxze rxew vxoc")
mailer = Mailer("smtp.gmail.com", 587, "snehayadav1109@gmail.com",password )
to_emails = ["sahpreeti206@gmail.com", "abdhesh102@gmail.com"]

subject = "Monthly Albums Report"
body="Hello,\n\nPlease find attached monthly report generated from SQLite database.\n\nRegards,\nSneha Yadav."
mailer.send_mail(
    to_emails,
    subject,
    body,
    attachments=[csv_path],
)
print("Email sent successfully 😃")
