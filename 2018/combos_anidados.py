# -*- coding:utf-8 -*-
from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Combos anidados", size=(400, 300))
        p = self.p = Panel(f, -1)
        provList = [u"Córdoba", "Buenos Aires", "San Luis"]
        ciudList = self.ciudList = [[u"Río Cuarto", "San Francisco", "Holmberg"], ["Pilar", "3 de Febrero"], ["Merlo", "Mercedes", "San Luis"]]
        cb1 = self.cb1 = ComboBox(self.p, -1, "Provincia", (10, 10), DefaultSize, provList, CB_DROPDOWN)
        self.indi = 0
        #cb2 = self.cb2 = TextCtrl(self.p, -1, "", (210, 10), (100,20))
        cb2 = self.cb2 = StaticText(self.p, -1, "", (210, 10), (100,20))
        cb1.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        f.Show()
        return True

    def OnKillFocus(self, e):
        self.indi = self.cb1.GetCurrentSelection()
        self.cb2.Destroy()
        self.cb2 = ComboBox(self.p, -1, "Ciudad", (210, 10), (100,20), self.ciudList[self.indi], CB_DROPDOWN)
        #print self.cb1.GetValue(), self.cb2.GetValue()
        e.Skip()


app = MiApp()
app.MainLoop()
