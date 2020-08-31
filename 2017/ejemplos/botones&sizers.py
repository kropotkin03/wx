import wx

class MyApp(wx.App):
	def OnInit(self):
		f = wx.Frame(None, -1, "")
		p = wx.Panel(f, -1)
		p.SetBackgroundColour("green")
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(wx.Button(p, -1, "An extremely long button text"), 1, wx.ALL, 10)
		b2 = wx.Button(p, -1, "Small Button")
		b2.SetBackgroundColour("red")
		sizer.Add(b2, 2, wx.ALL | wx.EXPAND, 10)
		p.SetSizer(sizer)
		f.Show()
		return True

app = MyApp(wx.App)
app.MainLoop()