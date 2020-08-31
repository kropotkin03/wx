from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None)
        f.Show()

        return True


app = MiApp()
app.MainLoop()
