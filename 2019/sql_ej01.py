import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()


cur.execute("INSERT INTO Gente(Nombre) VALUES ('pablokan')")
for x in range(3):
	nombre = input("Nombre: ")
	cur.execute("INSERT INTO Gente(Nombre) VALUES(?)", (nombre))

con.commit()
con.close()
