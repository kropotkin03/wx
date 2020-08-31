from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None)
        p = Panel(f)
        p.SetBackgroundColour("#ff00ff")
        t = StaticText(p, -1, "Hola mundo", size = (300, 300))
        f.Show()
        return True

app = MiApp()
app.MainLoop()
