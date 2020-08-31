import sqlite3

con = sqlite3.connect("base.db")
cur = con.cursor()

try:
    cur.execute("CREATE TABLE Gente (id	INTEGER NOT NULL PRIMARY KEY, Nombre TEXT, Edad INTEGER)")
except:
    pass


nombre = input("Nombre: ")
edad = 98
cur.execute("INSERT INTO Gente(nombre, edad) VALUES(?,?)", [nombre, edad])


con.commit()
con.close()

