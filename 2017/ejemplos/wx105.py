from wx import *

class MiApp(App):
    def OnInit(self):
        frame = Frame(None, -1, "nombre")
        frame.Show()
        panel = Panel(frame, -1, size = (300,100))
        caja = BoxSizer(HORIZONTAL)
        entrada = TextCtrl(panel,-1,value="Ingrese un texto:")
        boton = Button(panel,-1,label="Pulsame !")
        caja.Add(entrada, 1)
        caja.Add(boton, 1)
        panel.SetSizer(caja)
        panel.Layout()
        return True

app = MiApp()
app.MainLoop()











