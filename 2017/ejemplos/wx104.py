from wx import *

class MiApp(App):
    def OnInit(self):
        frame = Frame(None, -1, "nombre")
        frame.Show()
        panel = Panel(frame, -1, size = (300,100))
        cartel = StaticText(panel, label="Cartelito", pos=(20, 30))
        cartel.Show()

        return True

app = MiApp()
app.MainLoop()
