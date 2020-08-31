from  wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Anikka Albrite", size = (500, 800))
        b = Button(f, -1, "")
        b.SetBitmap(BitmapFromImage(Image("anikka.jpg")))
        b.Bind(EVT_BUTTON, self.click)
        f.Show()
        return True

    def click(self, event):
        pass

app = MiApp()
app.MainLoop()