from wx import *
import time

class MyApp(App):
    def OnInit(self):
        f = Frame(None,-1,"",size=(400,400))

        image_file = 'river.jpg'
        bmp1 = Image(image_file, BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = StaticBitmap(frame1, -1, bmp1, (0, 0))

        self.h=Button(f,-1,"",size=(100,100),pos=(0,200))
        self.h.Show(False)
        #Process the EVT_ENTER_WINDOW and EVT_LEAVE_WINDOW events
        self.b.Bind(EVT_ENTER_WINDOW, self.arriba)
        self.b.Bind(EVT_LEAVE_WINDOW, self.afuera)
        f.Show()
        return True

    def arriba(self, e):
        self.h.Show(True)

    def afuera(self, e):
        self.h.Show(False)


app = MyApp()
app.MainLoop()