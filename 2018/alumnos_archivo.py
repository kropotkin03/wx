# -*- coding:utf8 -*-
from wx import *
#import wx.dataview as dv
from wx.dataview import DataViewListCtrl


class MiApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Listado de Alumnos", size=(670, 500))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc = dvlc = DataViewListCtrl(p1)
        encabezado = [('DNI', 130), ('Nombre', 250), ('Comisión', 75), ('Sexo', 75), ('F.Nac', 100)]
        for enca in encabezado:
            dvlc.AppendTextColumn(enca[0], width=enca[1])
        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Carga de archivo")
        #bf = Button(p1, -1, "Nada")
        hor.Add(b)
        #hor.Add(bf)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.cargaArchivo)
        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()
        return True

    def cargaArchivo(self, e):
        lista = []
        with open("alumnos-python.csv", "r+") as archivo:
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


prog = MiApp()
prog.MainLoop()
