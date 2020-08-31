 # -*- coding:utf-8 -*-

from wx import *
from wx.dataview import *

class MyApp(App):
    def OnInit(self):
        f1= Frame(None,-1,"LISTA DE ALIMENTOS CARGADOS- proporción valores: 100gr", size = (1500,800))
        p1= self.p1 = Panel(f1,-1)
        self.dvlc= dvlc= DataViewListCtrl(p1)
        encabezado =[('ALIMENTO',400), ('KCALORIAS', 100), ('HIDRATOS-gr-', 100), ('PROTEÍNAS-gr-', 100), ('LIPIDOS-gr-',100)]
        for enca in encabezado:
            dvlc.AppendTextColumn (enca[0], width= enca[1])
        hor =BoxSizer(HORIZONTAL)
        #BOTONES
        b6= self.b6= Button(p1, -1, "&Cargar archivo")
        b1= self.b1= Button(p1, -1, "&Alta")
        b2= self.b2= Button(p1, -1, "&Baja")
        b3= self.b3= Button(p1, -1, "&Modificar")
        b4= self.b4= Button(p1, -1, "&Buscar")
        b5= self.b5= Button(p1, -1, "&Filtrar")

        #BINDEO
        b1.Bind(EVT_BUTTON, self.DarAlta)
        b6.Bind(EVT_BUTTON, self.CargaArchivo)

        sizer= BoxSizer (VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)

        hor.Add(self.b6)
        hor.Add(self.b1)
        hor.Add(self.b2)
        hor.Add(self.b3)
        hor.Add(self.b4)
        hor.Add(self.b5)

        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()

        return True

    def CargaArchivo(self, e):
        lista = []
        with open("TABLITAX.csv", "r+") as archivo:
            first = True
            for line in archivo:
                if first:
                    first = False
                else:
                    print line,
                    line = line[:-1]
                    lista.append(line)

        for e in lista:
            e = e.split(",")
            print e
            e.pop(0)
            print e

            self.dvlc.AppendItem(e)


    def DarAlta(self,event):
        f2= self.f2 = Frame (None, -1, "Cargar NUEVO alumno", size=(400,420))
        p2= self.p2 = Panel(f2, -1)
        sizer2 = BoxSizer(VERTICAL)

        StID= self.StID = StaticText(p2, -1, "ID ")
        TcID= self.TcID = TextCtrl(p2, -1, "ID")
        StDNI= self.StDNI = StaticText(p2, -1, "DNI ")
        TcDNI= self.TcDNI = TextCtrl(p2, -1, "DNI")
        StN= self.StN = StaticText(p2, -1, "NOMBRE ")
        TcN= self.TcN = TextCtrl(p2, -1, "NOMBRE")
        StC= self.StC = StaticText(p2, -1, "COMISIÓN ")
        TcC= self.TcC = TextCtrl(p2, -1, "COMISIÓN")
        StS= self.StS = StaticText(p2, -1, "SEXO ")
        TcS= self.TcS = TextCtrl(p2, -1, "SEXO")
        StF= self.StF = StaticText(p2, -1, "FECHA NACIMIENTO ")
        TcF= self.TcF = TextCtrl(p2, -1, "FECHA NACIMIENTO")
        sizer2.Add(self.StID, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.TcID, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.StDNI, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.TcDNI, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.StN, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.TcN, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.StC, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.TcC, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.StS, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.TcS, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.StF, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.TcF, 0, ALIGN_LEFT | ALL, 3)
        b7= self.b7 = Button (p2,-1, "Aceptar")
        b7.Bind (EVT_BUTTON, self.AceptarCarga)
        b8= self.b8 = Button (p2,-1, "Cancelar")
        b8.Bind(EVT_BUTTON, self.CancelarCarga)
        sizer2.Add(self.b7, 0 , ALIGN_CENTER | ALL, 4)
        sizer2.Add(self.b8, 0 , ALIGN_CENTER | ALL, 4)
        p2.SetSizer(sizer2)
        f2.Show()
        return True


    def AceptarCarga(self,event):
        Id = self.TcID.GetValue()
        Dni = self.TcDNI.GetValue()
        Nom = self.TcN.GetValue()
        Com = self.TcC.GetValue()
        Sex = self.TcS.GetValue()
        Fec = self.TcF.GetValue()
        with open("alumnos-python.csv", "a") as archivo:
            archivo.write(Id+",")
            archivo.write(Dni+",")
            archivo.write(Nom+",")
            archivo.write(Com+",")
            archivo.write(Sex+",")
            archivo.write (Fec+"\n")
        self.f2.Close()


    def CancelarCarga(self,event):
        self.f2.Close()

    #def DarBaja (self,event):
        f3 = self.f3 = Frame (None,-1,"Dar de baja alumno")
        p3 = self.panelp3 = Panel (f3)
        sizerBa = self.sizerBa = BoxSizer (VERTICAL)
        cartel = StaticText (panelBa, -1, "Ingrese el ID del alumno que desea dar de baja.")
        bajaID = self.bajaID = TextCtrl (panelBa, -1 , "ID")
        botonBaja = self.botonBaja = Button(panelBa,-1,"&Aceptar")
        botonBaja.Bind(EVT_BUTTON,self.cAceptar2)
        sizerBa.Add(cartel,0, ALIGN_CENTER | ALL, 2)
        sizerBa.Add(bajaID,0, ALIGN_CENTER | ALL, 2)
        sizerBa.Add(botonBaja,0, ALIGN_CENTER | ALL, 2)
        panelBa.SetSizer(sizerBa)
        frameBa.Show()





prog = MyApp()
prog.MainLoop()
