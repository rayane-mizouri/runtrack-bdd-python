import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="laplateforme"
)

cursor = db.cursor()

query = "SELECT SUM(superficie) AS superficie_totale FROM etage"
cursor.execute(query)

result = cursor.fetchone()
superficie_totale = result[0]

print("La superficie de La Plateforme est de", superficie_totale, "m2")

cursor.close()
db.close()