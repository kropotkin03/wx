# -*- coding:utf8 -*-
from wx import *

class MiApp(App):
    def OnInit(self):
        vent = Frame(None, -1, "control de teclas")
        self.entrada1 = TextCtrl(vent,-1,value="")
        self.entrada1.Bind(EVT_CHAR, self.teclazo)
        vent.Show()
        return True

    def teclazo(self, event):
        if 48 <= event.GetKeyCode() <= 57:
            event.Skip()
        else:
            print event.GetKeyCode()

app = MiApp()
app.MainLoop()
