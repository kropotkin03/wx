# -*- coding:utf8 -*-
from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Combos anidados", size=(400, 300))
        p = self.p = Panel(f, -1)
        gbs = self.gbs = GridBagSizer(20,20)
        provList = [u"Córdoba", "Buenos Aires", "San Luis"]
        ciudList = self.ciudList = [[u"Río Cuarto", "San Francisco", "Holmberg"], ["Pilar", "3 de Febrero"], ["Merlo", "Mercedes", "San Luis"]]
        cb1 = self.cb1 = ComboBox(self.p, -1, value = "Provincia", choices = provList, style = CB_DROPDOWN)
        self.indi = 0
        cb2 = self.cb2 = ComboBox(self.p, -1, value = "Ciudad", choices = ciudList[self.indi], style = CB_DROPDOWN)
        gbs.Add(cb1, pos = (0, 0))
        gbs.Add(cb2, pos = (0, 1))
        p.SetSizer(gbs)
        cb1.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        f.Show()
        return True

    def OnKillFocus(self, e):
        self.indi = self.cb1.GetCurrentSelection()
        self.cb2.Destroy()
        self.cb2 = ComboBox(self.p, -1, value = "Ciudad", choices = self.ciudList[self.indi], style = CB_DROPDOWN)
        self.gbs.Add(self.cb2, pos = (0, 1))
        self.p.Layout()
        print self.indi
        e.Skip()


app = MiApp()
app.MainLoop()
