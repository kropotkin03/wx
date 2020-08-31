from wx import *

class MyApp(App):
    def OnInit(self):

        f = Frame(None, -1, "GridBagSizer")
        p = Panel(f, -1, style = wx.TAB_TRAVERSAL)
        gbs = self.gbs = GridBagSizer(5, 5)
        for x in range(5):
            tc = TextCtrl(p, x, "")
            gbs.Add(tc , (x,x), flag=EXPAND )

        box = BoxSizer()
        box.Add(gbs, 1, ALL|EXPAND, 10)
        p.SetSizer(box)
        f.SetClientSize(p.GetBestSize())
        f.Show()
        return True

app = MyApp()
app.MainLoop()