import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()

try:
    cur.execute("CREATE TABLE Gente (Id INTEGER PRIMARY KEY, Nombre NVARCHAR)")
except:
    pass

cur.execute("INSERT INTO Gente (Nombre) VALUES ('Evangelina')")

for x in range(3):
	nombre = input("Nombre: ")
	cur.execute("INSERT INTO Gente(Id, Nombre) VALUES(?,?)", (x+11,nombre))

cur.execute("INSERT INTO Gente(Nombre) VALUES ('pablokan')")

con.commit()
con.close()

