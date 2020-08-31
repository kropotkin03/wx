import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()

cur.execute("SELECT Nombre, Edad FROM Gente ORDER BY Nombre")

rows = cur.fetchall()
for row in rows:
    print(row)

con.close()

