import wx

class MyApp(wx.App):
    def OnInit(self):
        f = wx.Frame(None)
        b = wx.Button(f)
        f.Show()
        b.Bind(wx.EVT_RIGHT_DOWN, self.onRclick)

        return True

    def onRclick(self, e):
        wx.MessageBox("click derecho")

app = MyApp()
app.MainLoop()
