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
        self.t = t = TextCtrl(f, value="Resultado", size=(100, 100), style=TE_READONLY)
        s.Add(n1, 1, EXPAND|ALL, 10)
        s.Add(n2, 1, EXPAND|ALL, 10)
        s.Add(b, 3, EXPAND|ALL, 10)
        s.Add(t, 1, EXPAND|TOP|LEFT|RIGHT, 25)
        f.Show()
        f.SetSizer(s)
        return True


    def bONf(self, event):
        self.b.SetBackgroundColour((0,255,200)) 
        
    def suma(self, event):
        s = str(int(self.n1.GetValue()) + int(self.n2.GetValue()))
        s = "Resultado = " + s
        self.t.SetValue(s)
        

app = MyApp()
app.MainLoop()
