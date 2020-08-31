# -*- coding:utf8 -*-
from wx import *

class MiApp(App):
    def OnInit(self):
        vent = Frame(None, -1, "g1e01")
        grilla = GridSizer(5,5,3,3)
        self.entrada1 = TextCtrl(vent,-1,value="")
        grilla.Add(self.entrada1)
        self.entrada1.Bind(EVT_CHAR, self.EvtChar)
        self.entrada2 = TextCtrl(vent,-1,value="")
        grilla.Add(self.entrada2)
        boton = Button(vent,-1,label="Suma")
        grilla.Add(boton)
        boton.Bind (EVT_BUTTON, self.CliqueaBoton)
        self.etiqueta = StaticText(vent,-1,label=u'')
        grilla.Add(self.etiqueta)
        vent.SetSizer(grilla)
        vent.Fit()
        vent.Show(True)
        return True

    def EvtChar(self, event):
        #self.log.WriteText('EvtChar: %d\n' % event.GetKeyCode())
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
