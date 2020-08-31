# -*- coding:utf8 -*-

class Empleado():
    def setDatosBasicos(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def getDatos(self):
        return self.nombre, self.sueldo

class Programador(Empleado):
    def __init__(self, lenguaje):
        self.lenguaje = lenguaje

    def setProyecto(self, proyecto, situacion):
        if proyecto != "":
            self.proyecto = proyecto
        self.situacion = situacion
    def getProyecto(self):
        return self.proyecto, self.situacion, self.lenguaje

class Administrativo(Empleado):
    def __init__(self, tAdmin):
        self.ingles = ""
        if tAdmin == "Secretaria":
            ingles = ""
            while ingles not in ["s", "n"]:
                ingles = raw_input("Sabe inglés: (s/n): ")
            self.ingles = ingles
    def sabeIngles(self):
        if self.ingles == "s":
            return "sabe inglés"
        else:
            return "no sabe inglés"


class Empresa():
    def __init__(self, nombre, rubro):
        listaProyectos = self.listaProyectos = ["Web Empresa Pollitos SA", "Sistema Empresa Gallina SRL"]
        listaLenguajes = self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML&CSS"]
        listaProgramadores = self.listaProgramadores = []
        listaAdministrativos = self.listaAdministrativos = []
        self.nombre = nombre
        self.rubro = rubro
    def getEmpresa(self):
        return self.nombre, self.rubro

    def agEmp(self, tipo):
        if tipo == "Programador":
            leng = raw_input("Que lenguaje maneja el candidato: ")
            prog = 0
            if leng in self.listaLenguajes:
                prog = Programador(leng)
                n = raw_input("Nombre: ")
                if leng == "Python":
                    s = 25000
                else:
                    s = 17000
                prog.setDatosBasicos(n, s)
                for p in self.listaProyectos:
                    print p
                np = raw_input("Proyecto? (1 o 2)")
                prog.setProyecto(self.listaProyectos[int(np)-1], "sin comenzar")
                self.listaProgramadores.append(prog)
            else:
                print "No se requiere personal para ese lenguaje"
                print "Los lenguajes requeridos son:", self.listaLenguajes
        else:
            SoC = raw_input("Secretaria o Cobranza (s/c): ")
            if SoC == "s":
                secOcob = "Secretaria"
            else:
                secOcob = "Cobranza"
            admi = Administrativo(secOcob)
            n = raw_input("Nombre: ")
            s = 8500
            admi.setDatosBasicos(n, s)
            self.listaAdministrativos.append(admi)



    def mostrarTodo(self):
        print self.getEmpresa()
        x = 0
        for pr in self.listaProgramadores:
            x += 1
            print x, pr.getDatos(), pr.getProyecto()
        for ad in self.listaAdministrativos:
            print ad.getDatos(), ad.sabeIngles()


empresa = Empresa("PabloKaniefsky", "Desarrollo de Software")
op = ""

while op != "4":
    print "Menu de Opciones"
    print "1 - Agregar empleado"
    print "2 - Modificar situación de proyecto"
    print "3 - Mostrar todo"
    print "4 - Salir"
    op = raw_input("Opción: ")
    if op == "1":
        op1 = ""
        while op1 not in ["1", "2"]:
            print "1 - Programador"
            print "2 - Administrativo"
            op1 = raw_input("Opción: ")

        if op1 == "1":
            empresa.agEmp("Programador")
        else:
            empresa.agEmp("Administrativo")

    elif op == "2":
        if len(empresa.listaProgramadores) != 0:
            empresa.mostrarTodo()
            opp = raw_input("Proyecto: ")
            listaSituaciones = ["", "En Proceso", "Atrasado", "Terminado"]
            sit = raw_input("Situación (1 - En Proceso, 2 - Atrasado, 3 - Terminado: ")
            empresa.listaProgramadores[int(opp)-1].setProyecto("", listaSituaciones[int(sit)])


    elif op == "3":
        empresa.mostrarTodo()











