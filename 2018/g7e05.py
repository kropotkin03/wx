from wx import *

class Asignatura():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def setNota(self, nota):
        self.nota = nota
    def getNota(self):
        return self.nota
    def condicion(self):
        resul = ""
        if self.nota >=4:
            resul = "Aprobado"
        else:
            resul = "Reprobado"
        return resul
    def nombreMateria(self):
        return self.nombre

class Alumno():
    listaMaterias = []
    listaNombreMaterias = []
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setEdad(self, edad):
        self.edad = edad
    def getEdad(self):
        return self.edad
    def addMateria(self, nombre, nota):
        materia = Asignatura(nombre, nota)
        if nombre not in self.listaNombreMaterias:
            self.listaMaterias.append(materia)
            self.listaNombreMaterias.append(nombre)
    def getMaterias(self):
        for m in self.listaMaterias:
            print m.nombre, m.nota, m.condicion()
    def promedio(self):
        acum = 0.0
        for n in self.listaMaterias:
            acum += n.nota
        return acum / len(self.listaMaterias)


class App():

    def __init__(self):
        a1 = Alumno("Juan", 25)
        a2 = Alumno("Ana", 19)
        a3 = Alumno("Pepe", 21)

        a1.addMateria("Python", 10)
        a1.addMateria("Ingles", 6)
        a1.addMateria("Lengua", 3)
        a1.addMateria("Python", 9)

        print a1.getNombre()
        print a1.getEdad()
        a1.getMaterias()
        print a1.promedio()

apli = App()






