# genérico para BD SQLite
import sqlite3

def alta()
con = sqlite3.connect("base.db")
cur = con.cursor()

try:
    cur.execute("CREATE TABLE Gente (Id	INTEGER NOT NULL PRIMARY KEY, Nombre TEXT, Edad INTEGER)")
except:
    pass


nombre = input("Nombre: ")
edad = 9
cur.execute("INSERT INTO Gente(Nombre, Edad) VALUES(?,?)", [nombre, edad])


con.commit()
con.close()

