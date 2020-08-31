from pkpy import *

class MyApp(App):
    def OnInit(self):
        b = BoxSizer(VERTICAL)
        p = PKpanel("newframe")
        p.SetBackgroundColour("green")
        t = StaticText(p, -1, "Primer panel")
        f[0].Show()
        print f[0].GetName()
        p2 = PKpanel("otroframe")

        p.SetBackgroundColour("red")
        t2 = StaticText(p2, -1, "Segundo panel")
        f[1].Show()
        b.Add(p,1)
        b.Add(p2,1)
        f[0].SetSizer(b)
        f[0].Layout()

        return True

app = MyApp()
app.MainLoop()
