import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()
parte = "an"
sentencia = "SELECT Nombre FROM Gente WHERE Nombre LIKE '%" + parte + "%' ORDER BY Nombre"
print(sentencia)
cur.execute(sentencia)

rows = cur.fetchall()
for row in rows:
    print(row[0])

con.close()

