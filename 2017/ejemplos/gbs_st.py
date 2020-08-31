from wx import *

class MyApp(App):
    def OnInit(self):

        f = Frame(None, -1, "GridBagSizer")
        p = Panel(f, -1)
        tcv = TextCtrl(p)
        gbs = GridBagSizer(15, 15)
        for x in range(5):
            tc = TextCtrl(p)
            gbs.Add(tc , (x,x), flag=EXPAND )
        tc = TextCtrl(p)
        gbs.Add(tc, (0,3 ),flag =EXPAND)

        p.SetSizer(gbs)
        f.SetClientSize(p.GetBestSize())
        gbs.Add(tcv, (1, 3), flag=EXPAND)
        f.Show()

        return True

app = MyApp()
app.MainLoop()