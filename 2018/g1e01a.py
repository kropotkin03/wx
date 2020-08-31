# -*- coding:utf8 -*-
from wx import *

class MiApp(App):
    def OnInit(self):
        vent = Frame(None, -1, "g1e01")
        grilla = GridSizer(3,3,5,5)
        self.entrada1 = TextCtrl(vent,-1,value="")
        grilla.Add(self.entrada1,0,0)
        self.entrada2 = TextCtrl(vent,-1,value="")
        grilla.Add(self.entrada2,0,1)
        boton = Button(vent,-1,label="Suma")
        grilla.Add(boton, 1,0)
        boton.Bind (EVT_BUTTON, self.CliqueaBoton)
        self.etiqueta = StaticText(vent,-1,label=u'')
        grilla.Add(self.etiqueta, 1,1 )
        vent.SetSizer(grilla)
        vent.Fit()
        vent.Show(True)
        return True

    def CliqueaBoton(self,event):
        n1 = int(self.entrada1.GetValue())
        n2 = int(self.entrada2.GetValue())
        salida = n1 + n2
        salida = "La suma es: " + str(salida)
        self.etiqueta.SetLabel(salida)

app = MiApp()
app.MainLoop()
