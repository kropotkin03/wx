from wx import *

class MyApp(App):
    def OnInit(self):

        f = Frame(None, -1, "GridBagSizer")
        gbs = self.gbs = GridBagSizer(5, 5)
        for x in range(5):
            tc = TextCtrl(f, x, "")
            gbs.Add(tc , (x,x), flag=EXPAND )

        box = BoxSizer()
        box.Add(gbs, 1, ALL|EXPAND, 10)
        f.SetSizer(box)
        f.Show()
        return True

app = MyApp()
app.MainLoop()