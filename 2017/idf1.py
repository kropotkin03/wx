from wx import *

class MyApp(App):
    def OnInit(self):
        frame1 = Frame(None, -1, "", size=(512, 512))
        image_file = 'river.jpg'
        bmp1 = Image(image_file, BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = StaticBitmap(frame1, -1, bmp1, (0, 0))
        self.button1 = Button(self.bitmap1, label='Button1', pos=(10, 10), size = (200, 200))
        self.button1.SetBitmap(BitmapFromImage(Image("carita.jpg", BITMAP_TYPE_ANY)))
        self.button2 = Button(self.bitmap1, label='Button2', pos=(310, 10))
        frame1.Show(True)
        return True

app = MyApp()
app.MainLoop()
