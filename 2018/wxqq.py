import wx


class MiApp (wx.App):
    def OnInit(self):
        v = wx.Frame(None, -1, "venti", size = (400,400))
        p = wx.Panel(v, -1, size = (200,100))
        p.SetBackgroundColour("RED")
        g = wx.GridBagSizer(1,10)
        c = wx.TextCtrl(p, -1, "ingrese nombre")
        g.Add(c, pos = (0,0))
        t = wx.StaticText(p, -1, "Hola mundo")
        g.Add(t, pos = (0,1))
        p.SetSizer(g)
        v.Show()
        return True


app = MiApp()
app.MainLoop()