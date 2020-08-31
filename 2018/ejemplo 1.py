import sqlite3
def crearBase():
    con = sqlite3.connect("baseEj.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE tablaEj(Id INTEGER PRIMARY KEY, Nombre TEXT, Apellido TEXT, DNI INTEGER)")
    except:
        pass
    con.close()
def cargarBase(nom,ape,dni):
    con = sqlite3.connect("baseEj.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO tablaEj(Nombre, Apellido, DNI)VALUES (?,?,?)",(nom,ape,dni))
    con.commit()
    con.close()
crearBase()
print ("Nombre: ")
n=raw_input()
print ("Apellido: ")
a=raw_input()
print ("Dni: ")
d=int(raw_input())
cargarBase(n,a,d)
