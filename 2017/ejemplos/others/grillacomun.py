from wx import *

class A(App):
    def OnInit(self):
        f = Frame(None)
        g = grid()



        f.Show()
        return True


a = A()
a.MainLoop()

