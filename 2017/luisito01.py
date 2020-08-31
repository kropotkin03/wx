import wx

class A(wx.App):
    def OnInit(self):
        f = wx.Frame(None)
        bmp = wx.Bitmap("river.jpg", wx.BITMAP_TYPE_JPG)
        mask = wx.Mask(bmp, wx.BLUE)

        bmp.SetMask(mask)
        b = wx.BitmapButton(f, -1, bmp, (20, 20), (bmp.GetWidth() + 10, bmp.GetHeight() + 10))
        b.SetToolTipString("This is a bitmap button.")
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)

        b = wx.BitmapButton(f, -1, bmp, (20, 120), style=wx.NO_BORDER)

        img = images.Robin.GetImage()
        cropped = img.GetSubImage((20, 20, bmp.GetWidth(), bmp.GetHeight()))
        b.SetBitmapSelected(cropped.ConvertToBitmap())

        b.SetToolTipString("This is a bitmap button with \nwx.NO_BORDER style.")
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)
        f.Show()
        return True


    def OnClick(self, event):
        pass


a = wx.App()
a.MainLoop()
