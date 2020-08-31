from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, size = (900, 500))
        # imagen de fondo
        image_file = 'bubble.png'
        bmp1 = Image(image_file, BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = StaticBitmap(f, -1, bmp1, (0, 0))
        # fin imagen de fondo
        pi = Panel(f, -1, size = (300, 500))
        pi.SetBackgroundColour('#ff0000')
        b1 = Button(pi)
        self.button1 = Button(pi, label='Button1', pos=(100, 10), size=(200, 200))
        self.button1.SetBitmap(Bitmap(Image("carita.jpg", BITMAP_TYPE_ANY)))
        pd = Panel(f, -1, size = (300, 500), pos = (601, 0))
        pd.SetBackgroundColour('#0000ff')
        b2 = Button(pd)

        f.Show()
        return True

app = MyApp()
app.MainLoop()
