import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="laplateforme"
)

cursor = db.cursor()

query = "SELECT nom, capacite FROM salles"
cursor.execute(query)

for row in cursor:
    print(f"('{row[0]}' - {row[1]})", end=", ")

cursor.close()
db.close()