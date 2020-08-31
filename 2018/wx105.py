from wx import *

class MiApp(App):
    def OnInit(self):
        frame = Frame(None, -1, "nombre")
        frame.Show()
        panel = Panel(frame, -1, size = (300,100))
        entrada = TextCtrl(panel,-1,value="Ingrese un texto:")
        boton = Button(panel,-1,label="Pulsame !")

        return True

app = MiApp()
app.MainLoop()











