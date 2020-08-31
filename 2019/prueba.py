from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        p = Panel(f)
        p.SetBackgroundColour((222, 89, 171 ))
        s = BoxSizer()
        self.b = b = Button(p, label="Hola")
        s.Add(b)
        b.Bind(EVT_BUTTON, self.ocultar)
        p.SetSizer(s)
        f.Show()
        return True

    def ocultar(self, e):
        print("voy a ocultar el botón")
        self.b.Show(False)

app = MyApp()
app.MainLoop()
