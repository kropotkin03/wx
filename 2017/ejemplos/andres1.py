from wx import *

class MiApp(App):
    def OnInit(self):

        f = Frame(None)
        caja = BoxSizer(VERTICAL)
        b = Button(f)
        caja.Add(b)
        b.Bind(EVT_BUTTON, self.accion)
        self.texto = TextCtrl(f)
        caja.Add(self.texto)
        f.SetSizer(caja)
        f.Show()
        return True

    def accion(self, event):
        self.texto.SetLabel("holanda")



app = MiApp()
app.MainLoop()
