import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="laplateforme"
)

cursor = db.cursor()

query = "SELECT SUM(capacite) AS capacite_total FROM salles"
cursor.execute(query)

result = cursor.fetchone()
capacite_total = result[0]

print("La capacité de toutes les salles est de", capacite_total)

cursor.close()
db.close()