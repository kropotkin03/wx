import wx

class MiApp(wx.App):
    def OnInit(self):
        f = wx.Frame(None, -1, "")
        p = wx.Panel(f, -1)
        p.SetBackgroundColour("#ff0000")
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)
        self.entrada1 = wx.TextCtrl(p,-1,value="uno")
        self.entrada2 = wx.TextCtrl(p,-1,value="dos")
        sizer.Add(self.entrada1)
        sizer.Add(self.entrada2)
        p.SetSizer(sizer)
        p.Fit()
        f.Show()
        return True

app = MiApp()
app.MainLoop()
