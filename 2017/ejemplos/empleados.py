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
            linea = linea[:-1] # le saco el barra ene, renegu�, ah, y le agregu� un enter al final pa no pensar
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

    def antiguedad(self, fIngreso):
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

    def tomoEmpleado(self, e):
        rEmp = self.dvlc.GetSelectedRow() # Registro de Empleado
        idEmp = self.empList[rEmp][0]
        nEmp = self.empList[rEmp][1]
        if idEmp not in self.empQueYaJugaron:
            self.empQueYaJugaron.append(idEmp)
            nPremio = random.randrange(1, 11)
            while  nPremio in self.premiosYaSalidos:
                nPremio = random.randrange(1, 11)
            self.premiosYaSalidos.append(nPremio)
            MessageBox(self.premios[nPremio], nEmp)

            # Bonus 1
            montoVenta = self.empList[rEmp][4]
            antig = self.antiguedad(self.empList[rEmp][2])
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
            mBonus1 = "Usted obtiene un Bonus 1 de " + str(bonus1)
            MessageBox(mBonus1, nEmp)

            # Bonus 2
            presentismo = self.empList[rEmp][3]
            if montoVenta > 150000:
                bonus2 = 3000 * presentismo / 100
            elif 75000 <= montoVenta <= 150000:
                bonus2 = 2000 * presentismo / 100
            else:
                bonus2 = 1000 * presentismo / 100
            mBonus2 = "Usted obtiene un Bonus 2 de " + str(bonus2)
            MessageBox(mBonus2, nEmp)
        else:
            MessageBox("Usted ya ha jugado!", nEmp)

prog = MiApp()
prog.MainLoop()
