#-*- coding:utf8 -*-
from wx import *
import wx.dataview as dv


class MiApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Registro de Trabajos", size = (850,600))
        p1 = self.p1 = Panel(f1, -1 )
        dvlc=self.dvlc= dv.DataViewListCtrl(p1)
        encabezado = [('Id',50), ('Equipo', 100), ('Descripcion', 200), ('Fec Evento', 100), ('Fec Reparacion', 100), ('Prioridad', 50), ('Estado', 50)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        sizer = wx.BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, wx.EXPAND)
        b = Button(p1, -1, "Registrar trabajo", size = DefaultSize )
        b.Bind(EVT_BUTTON, self.abrirAgP)
        sizer.Add(b)
        b2 = Button(p1, -1, "Actualizar", size = DefaultSize )
        b2.Bind(EVT_BUTTON, self.abrirMod)
        sizer.Add(b2)
        p1.SetSizer(sizer)
        f1.Show()
#        for id in range(1,10):
#            id= id +1
#        self.dvlc.AppendItem([id])

        return True
# End clase

#########  FIN DE LA APLICACION  ################



#funcion Abrir la carga de datos (Equipo, Descripcion, Fecha de evento, Prioridad, Operario designado, tipo de falla)
    def abrirAgP(self, e):
        f2 = Frame(None, -1, "Registar Trabajo", size = (350, 300))
        p2 = self.p2 = Panel(f2, -1, style = wx.TAB_TRAVERSAL)
        grilla = GridBagSizer(5,5)# tamaño de la grilla 5x5

    # Equipo -Texto Estatico y Caja de Texto
        equipo = StaticText(p2, -1, "Equipo")
        grilla.Add(equipo, pos = (0,0))
        equ = self.equ = TextCtrl(p2, -1, "Cargar Equipo")
        grilla.Add(equ, pos = (0,1), span = (1, 3))
    # Descripcion - Texto Estatico y  Caja de Texto
        desc= StaticText(p2, -1, "Descripcion del Evento")
        grilla.Add(desc, pos = (1,0))
        des= self.des =TextCtrl(p2, -1, "Completar")
        grilla.Add(des, pos = (1,1), span = (1, 3))
    # Fecha del Evento - Caja de Texto con fecha de hoy - Abre calendario
        l_fna = StaticText(p2, -1, "Fecha del Evento")
        grilla.Add(l_fna, pos = (2,0))
        hoy = str(DateTime.Today())
        hoy = hoy[3:5] + "/" + hoy[:2] + "/19" + hoy[6:8]
        print hoy
        fna =self.fna = TextCtrl(p2, -1, hoy)
        self.fna.Bind(EVT_LEFT_DOWN, self.abrirCal)
        grilla.Add(self.fna, pos = (2,1), span = (1, 3))
    # Prioridad - Lista desplegable
        prio = StaticText(p2, -1, "Prioridad")
        grilla.Add(prio, pos = (3,0))
        priList = ["Alta", "Media", "Baja"]
        pri = self.pri = ComboBox(p2, 500, "Prioridad", (90, 50), (160, -1), priList, CB_DROPDOWN | TE_PROCESS_ENTER )#Esta line me capta el valor que selec de la list desplegable
        grilla.Add(pri, pos = (3,1), span = (1, 3))
    # Tipo de Operario- CheckBoxes
        l_adi = StaticText(p2, -1, "Operario")
        grilla.Add(l_adi, pos = (4,0))
        adi1 = self.adi1 = CheckBox(p2, -1, "Plomero")
        adi2 = self.adi2 = CheckBox(p2, -1, "Albañil")
        adi3 = self.adi3 = CheckBox(p2, -1, "Gasista")
        grilla.Add(adi1, pos = (4, 1), span = (1, 1))
        grilla.Add(adi2, pos = (4, 2), span = (1, 1))
        grilla.Add(adi3, pos = (5, 1), span = (1,1))

    # Botón Guardar
        guardar = Button(p2, -1, "Guardar")
        grilla.Add(guardar, pos = (6, 0))# VER SI ACA ESTA EL PROBLEMA CUANDO GUARDO ...VER LAS POSICIONES
        guardar.Bind(EVT_BUTTON, self.guardaPart)

    # Muestra y ordena la grilla
        p2.SetSizerAndFit(grilla)
        f2.Show()
#########  FIN DE LA FUNCION DE CARGA DE DATOS################

# Funcion Guardar la Orden de Trabajo
    def guardaPart(self, evt):
        eq = self.equ.GetValue()# Equipo
        de = self.des.GetValue()# descripcion
        fn = self.fna.GetValue()# fecha evento
        pr = self.pri.GetValue()# Prioridad
        e= "Pendiente"#Estado de la OT


    # Secuencia de operario
        ad = ""
        if self.adi1.GetValue():
            ad += "Plomero"
        if self.adi2.GetValue():
            ad += " Albañil"
        if self.adi3.GetValue():
            ad += "Gasista"
    # Carga en la grilla
        self.dvlc.AppendItem([id,eq, de, fn,pr, ad,e])
        print self.dvlc
#..............................................................................

#Funcion para modificar la fila que voy a seleccionar

    def abrirMod(self, e):
        f3 = Frame(None, -1, "Actualiza Info", size = (350, 300))
        p3 = self.p3 = Panel(f3, -1, style = wx.TAB_TRAVERSAL)
        grilla1 = GridBagSizer(7,5)

        #Actualizar Equipo -Texto Estatico y Caja de Texto p/ Actualizar
        aequipo = StaticText(p3, -1, "Equipo")
        grilla1.Add(aequipo, pos = (0,0))
        aequ = self.aequ = TextCtrl(p3, -1)
        grilla1.Add(aequ, pos = (0,1), span = (1, 3))


#Actualizar Descripcion -Texto Estatico y Caja de Texto p/ Actualizar
        adescripcion = StaticText(p3, -1, "Descripcion")
        grilla1.Add(adescripcion, pos = (1,0))
        adescri = self.adescri= TextCtrl(p3, -1)
        grilla1.Add(adescri, pos = (1,1), span = (1, 3))

        # Coloca Fecha de la reparcion - Caja de Texto con fecha de hoy - Abre calendario
        al_fna = StaticText(p3, -1, "Fecha del Evento")
        grilla1.Add(al_fna, pos = (2,0))
        hoy = str(DateTime.Today())
        hoy = hoy[3:5] + "/" + hoy[:2] + "/19" + hoy[6:8]
        print hoy
        afna =self.afna = TextCtrl(p3, -1, hoy)
        self.afna.Bind(EVT_LEFT_DOWN, self.abrirCal)
        grilla1.Add(self.afna, pos = (2,1), span = (1, 3))

        # Cambiar la prioridad - Texto estatico y Cambio de Prioridad
        aprioridad = StaticText(p3, -1, "Prioridad ")
        grilla1.Add(aprioridad, pos = (3,0))
        apriList = ["Alta", "Media", "Baja"]
        apri = self.apri = ComboBox(p3, 500, "Prioridad Anterior", (90, 50), (160, -1), apriList, CB_DROPDOWN | TE_PROCESS_ENTER )#Esta line me capta el valor que selec de la list desplegable
        grilla1.Add(apri, pos = (3,1), span = (1, 3))

        # Actualiza el Estado- Texto estatico y Cambio de Estado
        aestado = StaticText(p3, -1, "Estado ")
        grilla1.Add(aestado, pos = (4,0))
        estadoList = ["En Curso", "Finalizado"]
        aesta = self.aesta = ComboBox(p3, 500, "Pendiente", (90, 50), (160, -1), estadoList, CB_DROPDOWN | TE_PROCESS_ENTER )#Esta line me capta el valor que selec de la list desplegable
        grilla1.Add(aesta, pos = (4,1), span = (1, 3))


# Botón Guardar Actualizacion
        aguardar = Button(p3, -1, "Guardar")
        grilla1.Add(aguardar, pos = (5, 0))
#        aguardar.Bind(EVT_BUTTON, self.aguardaPart)
        p3.SetSizerAndFit(grilla1)
        f3.Show()

###############################################  MODIFICAR
#GuardA los cambios
#    def aguardaPart(self, evt):
#        aeq = self.aequ.GetValue()# Equipo
#        ade = self.adescri.GetValue()# descripcion
#        afn = self.afna.GetValue()# fecha evento
#        apr = self.apri.GetValue()# Prioridad
#        aes = self.aesta.GetValue()# Estado


#        self.dvlc.AppendItem([id,aeq, ade, afn,apr, ad,aes])# Datos actualizados



#        lista=self.lista = self.dvlc.GetSelectedCols()
#        print lista
#        tCtrl(p3, -1, poslis)






# Begin Calendario
    def abrirCal(self, e):
        self.f3 = Frame(None, -1, "Calendario")
        g3 = GridSizer(0,0)
        cal = calendar.CalendarCtrl(self.f3, -1, DateTime.Today(), style=calendar.CAL_SEQUENTIAL_MONTH_SELECTION)
        g3.Add(cal)
        cal.Bind(calendar.EVT_CALENDAR, self.OnCalSelected)
        self.f3.SetSizerAndFit(g3)
        self.f3.Show()

    def OnCalSelected(self, e):
        #print('OnCalSelected: %s\n' % e.GetDate())
        hoy = str(e.GetDate())
        hoy = hoy[3:5] + "/" + hoy[:2] + "/19" + hoy[6:8]
        self.f3.Show(False)
        self.fna.SetValue(hoy)
# End Calendario

prog = MiApp()
prog.MainLoop()

