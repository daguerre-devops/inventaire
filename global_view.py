import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Exécution de la requête pour récupérer toutes les entrées de la table inventory
cursor.execute('SELECT * FROM inventory')
rows = cursor.fetchall()

# Affichage des résultats
for row in rows:
    print(row)

# Fermeture de la connexion
conn.close()
