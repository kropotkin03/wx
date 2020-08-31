from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1)
        p = Panel(f, -1)
        t = StaticText(p, -1, "holanda" )

        t.SetForegroundColour("red")
        t.SetBackgroundColour("green")
        f.Show()
        return True

app = MyApp()
app.MainLoop()
