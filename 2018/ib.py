from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame (None, -1, "")
        foto = "anikka.bmp"
        b = Button(f, -1, "")
        b.SetBitmap(foto)
        b.Bind(EVT_BUTTON, self.OnClick)
        f.Show()
        return True

    def OnClick(self, event):
        pass # hacer nada!



app = MiApp()
app.MainLoop()


