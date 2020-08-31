from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        f.SetBackgroundColour('#ff0000')

        # imagen de fondo

        p = Panel(f)
        imagen = Image("bubble.png", BITMAP_TYPE_ANY).ConvertToBitmap()
        bitmap1 = StaticBitmap(p, -1, imagen, (0, 0))
        # fin imagen de fondo

        f.Show()
        return True

app = MyApp()
app.MainLoop()
