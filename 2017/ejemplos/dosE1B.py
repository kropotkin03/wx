# -*- coding:utf8 -*-
from wx import *
from functools import partial

class MiApp(App):
    def OnInit(self):
        vent = self.vent = Frame(None, -1, "control de teclas")
        self.boton = Button(vent, size = (100, 50))
        caller()
        vent.Show()
        return True

def caller(self, event):
    if event.GetKeyCode() == ord("p"):
        self.boton.Bind(EVT_BUTTON, partial(self.teclazo, par1=self.boton, par2=self.bot2))

    def teclazo(self, event, par1, par2):

        par1.Hide()
        par2(None)

    def bot2(self, e):
        self.boton2 = Button(self.vent, label = "Porogna", size = (100, 50))
app = MiApp()
app.MainLoop()
