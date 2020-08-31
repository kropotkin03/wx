# -*- coding: cp1252 -*-
from wx import *
import wx.dataview as dv
import random

class MiApp(App):
    def OnInit(self):

        # Arreglos
        empList = self.empList = []
        empQueYaJugaron = self.empQueYaJugaron = []
        premiosYaSalidos = self.premiosYaSalidos = []
        premios = self.premios = ["", "Auto 0 km", "un Viaje a Bariloche para 2 personas", "un Viaje a Mar del Plata para 2 personas", "un Fin de semana en hotel spa para 2 personas", "una Cena para 2 personas"]
        for x in range(5):
            premios.append("Qu� l�stima, no consigui� ser TOP!")

        # Ventana Principal
        f1 = Frame(None, -1, "Listado de Vendedores", size = (1000,400))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc = dvlc = dv.DataViewListCtrl(p1)
        bSorteo = Button(p1, -1, "Sorteooooooo!!!!!")

        # Carga de datos desde archivo de texto
        archivo = open("empleados.csv")
        encabezado = archivo.readline()
        encabezado = encabezado.split(",")
        for enca in encabezado:
            dvlc.AppendTextColumn(enca, width=150)
        for linea in archivo:
            linea = linea[:-1] # le saco el bar ra ene, renegu�, ah, y le agregu� un enter al final pa no pensar
            linea = linea.split(",")
            for x in range(len(linea)):
                if x != 1:
                    linea[x] = int(linea[x])
            empList.append(linea)
            dvlc.AppendItem(linea) # AppendTextColumn para alinear bien pero.... naaaa
        archivo.close()

        # Layout
        caja = BoxSizer(VERTICAL)
        caja.Add(dvlc, 1, EXPAND)
        caja.Add(bSorteo, 0, ALL | EXPAND, 15)
        p1.SetSizer(caja)

        bSorteo.Bind(EVT_BUTTON, self.tomoEmpleado) # Enlace de bot�n con la funci�n de sorteo

        f1.Show()
        return True

    def tomoEmpleado(self, e):

        def salida(id, nombre, antig, premioTop, bonus1, bonus2 ):
            f2 = Frame(None, -1, "Cup�n de Premios", size = (900, 400))
            p2 = self.p1 = Panel(f2, -1 )
            p2.SetBackgroundColour("#c1ff55")
            fontResaltado = Font(15, FONTFAMILY_MODERN, FONTSTYLE_NORMAL, FONTWEIGHT_BOLD)
            fontPremio = Font(25, FONTFAMILY_DECORATIVE, FONTSTYLE_NORMAL, FONTWEIGHT_BOLD)
            t1s = "N�mero de Empleado: " + str(id)
            t1 = StaticText(p2, -1, t1s)
            t2 = StaticText(p2, -1, nombre)
            t2.SetFont(fontResaltado)
            t2.SetForegroundColour("red")
            t3s = "Antig�edad en la empresa: " + str(antig) + " a�os"
            t3 = StaticText(p2, -1, t3s)
            premioTop = StaticText(p2, -1, premioTop)
            premioTop.SetForegroundColour("#110196")
            premioTop.SetFont(fontPremio)
            bonus1 = StaticText(p2, -1, bonus1)
            bonus2 = StaticText(p2, -1, bonus2)
            cabeza = BoxSizer(HORIZONTAL)

            cabeza.Add(t1, 0, ALL | ALIGN_BOTTOM, 10)
            cabeza.Add(t2, 0,   ALL | ALIGN_BOTTOM, 10)
            cabeza.Add(t3, 0, ALL | ALIGN_BOTTOM, 10)
            caja = BoxSizer(VERTICAL)
            caja.Add(cabeza, 2, ALL | ALIGN_CENTER, 10)
            caja.Add(premioTop, 2, ALL | ALIGN_CENTER, 10)
            caja.Add(bonus1, 1, ALL | ALIGN_CENTER, 10)
            caja.Add(bonus2, 1, ALL | ALIGN_CENTER, 10)
            p2.SetSizer(caja)
            f2.Show()

        def antiguedad(fIngreso):
            from datetime import date
            fHoy = date.today()
            aHoy = fHoy.year
            mHoy = fHoy.month
            dHoy = fHoy.day
            fIng = str(fIngreso)
            aIng = int(fIng[:4])
            mIng = int(fIng[4:6])
            dIng = int(fIng[6:])
            antig = aHoy - aIng
            if (mIng > mHoy) or (mIng==mHoy and dIng > dHoy):
                antig -= 1
            return antig

        rEmp = self.dvlc.GetSelectedRow() # Registro de Empleado
        idEmp = self.empList[rEmp][0]
        nEmp = self.empList[rEmp][1]
        if idEmp not in self.empQueYaJugaron:
            self.empQueYaJugaron.append(idEmp)

            # Premio TOP
            nPremio = random.randrange(1, 11)
            while  nPremio in self.premiosYaSalidos:
                nPremio = random.randrange(1, 11)
            self.premiosYaSalidos.append(nPremio)

            # Bonus 1
            montoVenta = self.empList[rEmp][4]
            antig = antiguedad(self.empList[rEmp][2])
            sueldo = self.empList[rEmp][5]
            if montoVenta > 100000:
                if antig < 10:
                    bonus1 = sueldo * 0.15
                elif 10 <= antig <= 20:
                    bonus1 = sueldo * 0.10
                else:
                    bonus1 = sueldo * 0.05
            else:
                bonus1 = sueldo * 0.03
            mBonus1 = "Usted obtiene un Bonus 1 de " + str(bonus1) + " pesos"

            # Bonus 2
            presentismo = self.empList[rEmp][3]
            if montoVenta > 150000:
                bonus2 = 3000 * presentismo / 100
            elif 75000 <= montoVenta <= 150000:
                bonus2 = 2000 * presentismo / 100
            else:
                bonus2 = 1000 * presentismo / 100
            mBonus2 = "Usted obtiene un Bonus 2 de " + str(bonus2) + " pesos"

            #grabo
            descPremioTop = self.premios[nPremio]
            aSalida = open("salida.txt", "a")
            lineaSalida = str(idEmp) + "-" + nEmp + "-" + descPremioTop + "-" + str(bonus1) + "-" + str(bonus2) + "\n"
            aSalida.write(lineaSalida)
            salida(idEmp, nEmp, antig, descPremioTop, mBonus1, mBonus2 )

        else:
            MessageBox("Usted ya ha jugado!", nEmp)

prog = MiApp()
prog.MainLoop()
