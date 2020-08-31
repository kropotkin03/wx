from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Titulo")
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        t1 = self.t1 = TextCtrl(p)
        t2 = self.t2 = TextCtrl(p)
        b = Button(p, -1, "Suma")
        r = self.r = TextCtrl(p, style=TE_READONLY)
        b.Bind(EVT_BUTTON, self.sumar)
        s.Add(t1, 0, ALIGN_CENTER|ALL, 10)
        s.Add(t2, 0, ALIGN_CENTER|ALL, 10)
        s.Add(b, 0, ALIGN_CENTER|ALL, 10)
        s.Add(r, 0, ALIGN_CENTER|ALL, 10)
        p.SetSizer(s)
        f.Show()

        return True

    def sumar(self, e):
        self.r.SetLabel(str(int(self.t1.Value) + int(self.t2.Value)))


app = MyApp()
app.MainLoop()

