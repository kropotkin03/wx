import wx

class Panel1(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        image_file = 'river.jpg'
        bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap1 = wx.StaticBitmap(
        self, -1, bmp1, (0, 0))
        str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight())
        parent.SetTitle(str1)
        self.button1 = wx.Button(self.bitmap1, label='Button1', pos=(8, 8))

app = wx.App(False)
frame1 = wx.Frame(None, -1, "An image on a panel", size=(512, 512))
panel1 = Panel1(frame1, -1)
frame1.Show(True)
app.MainLoop()