from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        b = BoxSizer(VERTICAL)
        mas = True
        while mas:
            self.n1 = n1 = TextCtrl(f)
            b.Add(n1)
            self.n2 = n2 = TextCtrl(f)
            b.Add(n2)
            bSuma = Button(f, label = "Sumar")
            b.Add(bSuma)
            bSuma.Bind(EVT_BUTTON, self.suma)
            self.r = r = StaticText(f)
            b.Add(r)
        f.SetSizer(b)
        f.Show()
        return True

    def suma(self, event):
        r = str(int(self.n1.GetValue()) + int(self.n2.GetValue()))
        self.r.SetLabel(r)

app = MyApp()
app.MainLoop()
