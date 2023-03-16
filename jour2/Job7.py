import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def create(self, nom, prenom, salaire, id_service):
        cursor = self.db.cursor()
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        cursor.execute(query, values)
        self.db.commit()
        cursor.close()

    def read_all(self):
        cursor = self.db.cursor()
        query = "SELECT employes.nom, employes.prenom, employes.salaire, services.nom AS service FROM employes INNER JOIN services ON employes.id_service = services.id"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def update(self, id, nom, prenom, salaire, id_service):
        cursor = self.db.cursor()
        query = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (nom, prenom, salaire, id_service, id)
        cursor.execute(query, values)
        self.db.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.db.cursor()
        query = "DELETE FROM employes WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        self.db.commit()
        cursor.close()

    def __del__(self):
        self.db.close()

employe = Employe("localhost", "root", "password", "comptabilite")
employe.create("Nom", "Prenom", 5, 1)
employes = employe.read_all()
for employe in employes:
    print(f"{employe[0]} - {employe[1]} - {employe[2]} - {employe[3]}")
employe.update(1, "Nom", "Prénom", 55000, 2)
employe.delete(1)