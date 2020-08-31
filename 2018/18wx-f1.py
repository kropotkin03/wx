import wx


class MyApp(wx.App):
    def OnInit(self):
        f = self.f = wx.Frame(None)
        panel = wx.Panel(f, -1)
        button = wx.Button(panel, -1, "Cerrame")
        button.SetPosition((15, 15))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        f.Show()
        return True

    def OnCloseMe(self, event):
        self.f.Close(True)

    def OnCloseWindow(self, event):
        self.f.Destroy()


app = MyApp()
app.MainLoop()

