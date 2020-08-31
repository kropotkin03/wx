from wx import *

class MyApp(App):
    def OnInit(self):

        f = Frame(None, -1, "GridBagSizer")
        p = Panel(f)
        caja = BoxSizer(HORIZONTAL)

        self.tc = tc = TextCtrl(p)
        caja.Add(tc)
        self.st = st = StaticText(p, label = "papo")
        caja.Add(st)
        bo = Button(p)
        caja.Add(bo)
        bo.Bind(EVT_BUTTON, self.onC)
        p.SetSizer(caja)
        f.Show()

        return True

    def onC(self, e):
        self.tc.Destroy()
        self.st.Destroy()



app = MyApp()
app.MainLoop()