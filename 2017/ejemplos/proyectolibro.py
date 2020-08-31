#-*-coding:utf8-*-
from wx import *
import wx.dataview as dv

class MiApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Libro de IVA", size = (1040,500))
        p1 = self.p1 = Panel (f1,-1)
        self.dvlc = dvlc = dv.DataViewListCtrl(p1)
        encabezado = [("Nro Factura",100),("Fecha",80),("Cliente",200),("CUIT",100),("Tipo Factura",80),("Importe Neto",100),("% IVA",60),("IVA",80),("Valor no agravado",110),("Importe Bruto",100)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        sizer = wx.BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, wx.EXPAND)
        b = Button(p1, -1, "Agregar Factura", size = DefaultSize )
        b.Bind(EVT_BUTTON, self.abrirAgP)
        sizer.Add(b)
        p1.SetSizer(sizer)
        f1.Show()
        return True

    def abrirAgP(self, e):
        f2 = Frame(None, -1, "Ingreso de Factura", size = (350, 300))
        p2 = self.p2 = Panel(f2, -1, style = wx.TAB_TRAVERSAL)
        grilla = GridBagSizer(7,7)
# Numero de Factura - Caja de Texto
        l_fac = StaticText(p2, -1, "Número de Factura")
        grilla.Add(l_fac, pos = (0,0))
        fac = self.fac = TextCtrl(p2, -1, "Ingrese Nro")
        grilla.Add(fac, pos = (0,1), span = (1, 3))
# Fecha - Caja de Texto con fecha de hoy - Abre calendario
        l_fna = StaticText(p2, -1, "Fecha")
        grilla.Add(l_fna, pos = (1,0))
        hoy = str(DateTime.Today())
        hoy = hoy[3:5] + "/" + hoy[:2] + "/20" + hoy[6:8]
        print hoy
        fna =self.fna = TextCtrl(p2, -1, hoy)
        self.fna.Bind(EVT_LEFT_DOWN, self.abrirCal)
        grilla.Add(self.fna, pos = (1,1), span = (1, 3))
# Cliente - Caja de Texto
        l_cli = StaticText(p2, -1, "Cliente")
        grilla.Add(l_cli, pos = (2,0))
        cli = self.cli = TextCtrl(p2, -1, "Ingrese Cliente")
        grilla.Add(cli, pos = (2,1), span = (1, 3))
# CUIT - Caja de Texto
        l_cuit = StaticText(p2, -1, "CUIT")
        grilla.Add(l_cuit, pos = (3, 0))
        cuit = self.cuit =TextCtrl(p2, -1, "Ingrese CUIT")
        grilla.Add(cuit, pos = (3, 1), span = (1, 3))
# Tipo de Factura - Radio
        l_tipo = StaticText(p2, -1, "Tipo de factura")
        grilla.Add(l_tipo, pos = (4, 0))
        tipoList = ["A", "B", "C"]
        tipo = self.tipo = RadioBox(p2, -1, "", DefaultPosition, DefaultSize, tipoList, 3, NO_BORDER)
        grilla.Add(tipo, pos = (4, 1))
# Importe neto - Caja de Texto
        l_imp = StaticText(p2, -1, "Importe Neto")
        grilla.Add(l_imp, pos = (5, 0))
        imp = self.imp =TextCtrl(p2, -1, "Ingrese Importe")
        grilla.Add(imp, pos = (5, 1), span = (1, 3))
# Tipo de IVA - Radio Buttons
        l_iva = StaticText(p2, -1, "Tipo de IVA")
        grilla.Add(l_iva, pos = (6, 0))
        ivaList = ["21", "25"]
        iva = self.iva = RadioBox(p2, -1, "", DefaultPosition, DefaultSize, ivaList, 2, NO_BORDER)
        grilla.Add(iva, pos = (6, 1))

# Botón Guardar
        guardar = Button(p2, -1, "Guardar")
        grilla.Add(guardar, pos = (7, 0))
        guardar.Bind(EVT_BUTTON, self.guardaPart)

# Muestra la grilla
        p2.SetSizerAndFit(grilla)
        f2.Show()
# Guarda el participante
    def guardaPart(self, evt):
        fa = self.fac.GetValue()
        fn = self.fna.GetValue()
        cl = self.cli.GetValue()
        im = self.imp.GetValue()
        ti = self.tipo.GetString(self.tipo.GetSelection())
        cu = self.cuit.GetValue()
        iv = self.iva.GetString(self.iva.GetSelection())
        print fa, fn, cl, im, ti, cu, iv
        self.dvlc.AppendItem([fa, fn, cl, im, ti, cu, iv, "", "", ""])



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
        hoy = hoy[3:5] + "/" + hoy[:2] + "/20" + hoy[6:8]
        self.f3.Show(False)
        self.fna.SetValue(hoy)
# End Calendario


prog = MiApp()
prog.MainLoop()


