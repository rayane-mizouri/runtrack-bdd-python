import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="laplateforme"
)
print(db)

cursor = db.cursor()

query = "SELECT * FROM etudiants"
cursor.execute(query)

for row in cursor:
    print(f"{row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}")

cursor.close()
db.close()