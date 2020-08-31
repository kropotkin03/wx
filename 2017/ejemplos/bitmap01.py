from  wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Anikka Albrite", size = (500, 800))
        self.b = b = Button(f, -1, "")
        b.SetBitmap(Bitmap(Image("anikka.jpg")))
        b.Bind(EVT_BUTTON, self.cFondo)
        b.Bind(EVT_BUTTON, self.click)
        f.Show()
        return True

    def click(self, event):
        pass

    def cFondo(self, e):
        self.b.SetBitmap(Bitmap(Image("pppp.jpg")))


app = MiApp()
app.MainLoop()