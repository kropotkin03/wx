# -*- coding:utf8 -*-
from wx import *
import wx.dataview as dv

class MiApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Participantes", size = (850,600))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc = dvlc = dv.DataViewListCtrl(p1)
        encabezado = [('Apellido', 150), ('Nombre', 150), ('F.Nac.', 100), ('Especialidad', 150), ('Adicionales', 100), ('Importe', 100)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "Agregar participante", size = (200, 30) )
        b2 = Button(p1, -1, "Nada", size = (200, 30))
        hor.Add(b, 0, ALL | EXPAND, 10)
        hor.Add(b2, 0, ALL | EXPAND, 10)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        sizer.Add(hor, 0) # 0 ajusta!
        b.Bind(EVT_BUTTON, self.abrirAgP)
        b2.Bind(EVT_BUTTON, self.nadas)
        p1.SetSizer(sizer)
        p1.Layout()
        f1.Show()
        return True

    def nadas(self, e):
        print self.p1.GetId()
        print self.dvlc.GetValue(3, 1)



    def abrirAgP(self, e):
        f2 = Frame(None, -1, "Agregar participante", size = (350, 300))
        p2 = self.p2 = Panel(f2, -1, style = wx.TAB_TRAVERSAL)
        grilla = GridBagSizer(5,5)
# Apellido - Caja de Texto
        l_ape = StaticText(p2, -1, "Apellido")
        grilla.Add(l_ape, pos = (0,0))
        ape = self.ape = TextCtrl(p2, -1, "Apellido")
        grilla.Add(ape, pos = (0,1), span = (1, 3))
# Nombre - Caja de Texto
        l_nom = StaticText(p2, -1, "Nombre")
        grilla.Add(l_nom, pos = (1,0))
        nom = self.nom =TextCtrl(p2, -1, "Nombre")
        grilla.Add(nom, pos = (1,1), span = (1, 3))
# Fecha de Nacimiento - Caja de Texto con fecha de hoy - Abre calendario
        l_fna = StaticText(p2, -1, "Fecha de Nacimiento")
        grilla.Add(l_fna, pos = (2,0))
        hoy = str(DateTime.Today())
        hoy = hoy[3:5] + "/" + hoy[:2] + "/19" + hoy[6:8]
        print hoy
        fna =self.fna = TextCtrl(p2, -1, hoy)
        self.fna.Bind(EVT_LEFT_DOWN, self.abrirCal)
        grilla.Add(self.fna, pos = (2,1), span = (1, 3))
# Profesión - Combo
        l_pro = StaticText(p2, -1, "Especialidad")
        grilla.Add(l_pro, pos = (3,0))
        proList = ["Arquitecto", "Analista", "Soft Dev"]
        self.pro = cb = ComboBox(p2, 500, "Especialidad", (90, 50), (160, -1), proList, CB_DROPDOWN | TE_PROCESS_ENTER )
        cb.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        grilla.Add(self.pro, pos = (3,1), span = (1, 3))
# Adicionales - CheckBoxes
        l_adi = StaticText(p2, -1, "Adicionales")
        grilla.Add(l_adi, pos = (4,0))
        adi1 = self.adi1 = CheckBox(p2, -1, "Cena")
        adi2 = self.adi2 = CheckBox(p2, -1, "Sala VIP")
        grilla.Add(adi1, pos = (4, 1), span = (1, 1))
        grilla.Add(adi2, pos = (4, 2), span = (1, 1))
# Importe - Radio Buttons
        l_imp = StaticText(p2, -1, "Importe")
        grilla.Add(l_imp, pos = (5,0))
        impList = ["$80", "$150", "$200"]
        imp = self.imp = RadioBox(p2, -1, "", DefaultPosition, DefaultSize, impList, 2, NO_BORDER)
        grilla.Add(imp, pos = (5, 1))
# Botón Guardar
        guardar = Button(p2, -1, "Guardar")
        grilla.Add(guardar, pos = (6, 0))
        guardar.Bind(EVT_BUTTON, self.guardaPart)

# Muestra la grilla
        p2.SetSizerAndFit(grilla)
        f2.Show()
#Guarda el participante
    def guardaPart(self, evt):
        ap = self.ape.GetValue()
        no = self.nom.GetValue()
        fn = self.fna.GetValue()
        pr = self.pr = self.pro.GetValue()
        ad = ""
        if self.adi1.GetValue():
            ad += "Cena"
        if self.adi2.GetValue():
            ad += " VIP"
        im = self.imp.GetString(self.imp.GetSelection())
        self.dvlc.AppendItem([ap, no, fn, pr, ad, im])



# Begin Combo
    def OnKillFocus(self, evt):
        self.pr = self.pro.GetValue()
        evt.Skip()
# End Combo

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
        hoy = hoy[3:5] + "/" + hoy[:2] + "/" + hoy[6:8]
        self.f3.Show(False)
        self.fna.SetValue(hoy)
# End Calendario

prog = MiApp()
prog.MainLoop()
