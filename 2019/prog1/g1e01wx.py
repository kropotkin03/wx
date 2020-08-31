from wx import *
from validador import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(500, 100))
        s = BoxSizer()
        self.n1 = n1 = TextCtrl(f, validator=MyValidator())
        self.n2 = n2 = TextCtrl(f, validator=MyValidator())
        self.b = b = Button(f, label="Sumar")
        b.Bind(EVT_SET_FOCUS, self.bONf)
        b.Bind(EVT_BUTTON, self.suma)
        self.t = t = StaticText(f, label="Resultado", size=(100, 100))
        s.Add(n1, 1, EXPAND|ALL, 10)
        s.Add(n2, 1, EXPAND|ALL, 10)
        s.Add(b, 3, EXPAND|ALL, 10)
        s.Add(t, 1, EXPAND|TOP|LEFT|RIGHT, 25)
        f.SetSizer(s)
        f.Show()
        return True


    def bONf(self, event):
        self.b.SetBackgroundColour((0,255,200)) 
        
    def suma(self, event):
        s = str(int(self.n1.GetValue()) + int(self.n2.GetValue()))
        s = "Resultado = " + s
        self.t.SetLabel(s)
        self.t.SetForegroundColour((255,0,0))
        

app = MyApp()
app.MainLoop()
