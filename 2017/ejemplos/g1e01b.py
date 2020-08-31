# -*- coding:utf8 -*-
from wx import *

class MiApp(App):
    def OnInit(self):
        vent = Frame(None, -1, "g1e01", style=DEFAULT_FRAME_STYLE ^ RESIZE_BORDER)
        grilla = GridBagSizer(5,5)

        self.entrada1 = TextCtrl(vent,-1,value="")
        grilla.Add(self.entrada1, pos=(0,0))
        self.entrada1.Bind(EVT_CHAR, self.teclazo)
        self.entrada2 = TextCtrl(vent,-1,value="")
        grilla.Add(self.entrada2, pos=(0,1))
        boton = Button(vent,-1,label="Suma")
        grilla.Add(boton, pos=(1,0), span=(1,2), flag=EXPAND)
        boton.Bind (EVT_BUTTON, self.CliqueaBoton)
        self.etiqueta = StaticText(vent,-1,label='')
        grilla.Add(self.etiqueta, pos=(2,1) )
        vent.SetSizer(grilla)
        vent.Fit()
        vent.Show()
        return True

    def teclazo(self, event):
        if event.GetKeyCode() == WXK_TAB:
            self.entrada2.SetFocus()
        else:
            event.Skip()

    def CliqueaBoton(self,event):
        n1 = int(self.entrada1.GetValue())
        n2 = int(self.entrada2.GetValue())
        salida = n1 + n2
        salida = "La suma es: " + str(salida)
        self.etiqueta.SetLabel(salida)

app = MiApp()
app.MainLoop()
