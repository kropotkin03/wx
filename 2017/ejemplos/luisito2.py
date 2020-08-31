from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, style = MAXIMIZE)
        f.SetBackgroundColour('#0000ff')

        # imagen de fondo
        image_file = 'bubble.png'
        bmp1 = Image(image_file, BITMAP_TYPE_ANY).ConvertToBitmap()
        bitmap1 = StaticBitmap(f, -1, bmp1, (0, 0))
        # fin imagen de fondo

        f.Show()
        return True

app = MyApp()
app.MainLoop()
