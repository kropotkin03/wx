from wx import *
from ordygrilla import *


class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(600, 400))
        Grillaza(f, 1, data=musicdata)
        f.Show()
        return True


a = MyApp()
a.MainLoop()
