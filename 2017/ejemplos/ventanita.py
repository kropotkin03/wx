from wx import *

class MiApp(App):
    def OnInit(self):
        estilos = RESIZE_BORDER | SYSTEM_MENU | CAPTION | CLOSE_BOX | CLIP_CHILDREN | FRAME_NO_TASKBAR
        f = Frame(None, -1, "ventanita", (200,0), size = (500, 700), style = estilos)
        f.Show()
        return True


app = MiApp()
app.MainLoop()
