from wx import *

class A(App):
    def OnInit(self):
        f = Frame(None)
        b1 = Button(f, -1, "boton1", pos = (5,5), size = (200, 100))
        b2 = Button(f, -1, "boton1", pos = (5, 125), size = (100, 200))
        f.Show()

        return True



a = A()
a.MainLoop()