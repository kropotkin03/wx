from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(1000, 1000))
        gbs = GridBagSizer(25, 50)

        for i in range(5):
            t = TextCtrl(f)
            gbs.Add(t, pos=(i,i))
        b = Button(f)
        gbs.Add(b, pos=(6,2))
        t = TextCtrl(f, style=TE_MULTILINE)
        gbs.Add(t, pos=(8,3), span=(18,2), flag=EXPAND)
        f.SetSizer(gbs)
        f.Show()
        return True



app = MyApp()
app.MainLoop()
