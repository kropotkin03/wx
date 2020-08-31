from wx import *

class MyApp(App):
    def OnInit(self):

        f = Frame(None, -1, "GridFlexSizer")
        p = Panel(f, -1)
        gbs = FlexGridSizer(2,3,13,13)
        for x in range(5):
            #tc = TextCtrl(p, -1, str(x))
            tc = StaticText(p, label = str(x), size = (200, 100))
            gbs.Add(tc)

        p.SetSizer(gbs)
        f.SetClientSize(p.GetBestSize())
        f.Show()
        return True

app = MyApp()
app.MainLoop()