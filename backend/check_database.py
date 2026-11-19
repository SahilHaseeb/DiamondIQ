
import sqlite3
from database import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()

cursor.execute("SELECT * FROM predictions")

records = cursor.fetchall()

print("\nDIAMONDIQ PREDICTION HISTORY ")

for record in records:
    print(record)

print("\nTotal Predictions:", len(records))

connection.close()
