import wx

labels = "one two three four five six seven eight nine".split()

class GridSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Basic Grid Sizer")
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)
        self.entrada1 = wx.TextCtrl(self,-1,value="uno")
        self.entrada2 = wx.TextCtrl(self,-1,value="dos")
        sizer.Add(self.entrada1, 0, 0)
        sizer.Add(self.entrada2, 0, 1)
        self.SetSizer(sizer)
        self.Fit()

app = wx.PySimpleApp()
GridSizerFrame().Show()
app.MainLoop()
