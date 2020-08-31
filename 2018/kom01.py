import wx

class MiApp(wx.App):
    def OnInit(self):
        f = wx.Frame(None, -1, "")
        p = wx.Panel(f, -1)
        t = wx.StaticText(p, -1, "hop")
        f.Show()
        return True
    
app = MiApp()
app.MainLoop()


