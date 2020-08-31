import wx

app = wx.App()

frame = wx.Frame(None, -1, 'ventanita', pos=(800,0), size=(200,600))
frame.Show()

app.MainLoop()
