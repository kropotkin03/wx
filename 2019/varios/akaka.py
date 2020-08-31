from wx import *

class MyApp(App):
    def OnInit(self):
        self.listaT = listaT = []
        f = Frame(None)
        s = BoxSizer(VERTICAL)
        for i in range(3):
            t = TextCtrl(f)
            s.Add(t, 0, ALL, 20)
            listaT.append(t)
        b = Button(f, label="botón")
        s.Add(b, 0, ALL, 20)
        b.Bind(EVT_BUTTON, self.muestro)
        f.SetSizer(s)
        f.Show()
        return True


    def muestro(self, event):
        for e in self.listaT:
            print(e.GetValue())

app = MyApp()
app.MainLoop()
