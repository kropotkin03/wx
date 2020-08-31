# -*- coding:utf8 -*-
from wx import *

class MiApp(App):
    def OnInit(self):
        vent = Frame(None)
        self.entrada1 = TextCtrl(vent)
        self.entrada1.Bind(EVT_CHAR, self.teclazo)
        vent.Show()
        return True

    def teclazo(self, event):

        print event.GetKeyCode()
        if 48 <= event.GetKeyCode() <= 57 or event.GetKeyCode() == 46:
             event.Skip()


app = MiApp()
app.MainLoop()
