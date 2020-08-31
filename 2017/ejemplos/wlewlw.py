from wx import *

class A(App):
    def OnInit(self):
        self.f = Frame(None)
        self.caja = TextCtrl(self.f, -1, "")
        boton = Button(self.f, -1, "buscar")
        self.texto = StaticText(self.f, -1, "          ")
        b = BoxSizer(VERTICAL)
        b.Add(self.caja)
        b.Add(boton)
        b.Add(self.texto)
        boton.Bind(EVT_BUTTON, self.obtRes)
        self.f.SetSizer(b)

        self.f.Show()
        return True

    def obtRes(self, e):
        e.
        buscar = self.caja.GetValue()
        self.texto.SetLabel(buscar)



a = A()
a.MainLoop()
