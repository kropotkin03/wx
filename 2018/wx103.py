import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (-1, -1), size =(250, 150))
        panel = wx.Panel(self, -1)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(wx.Button(panel, -1, 'Button1'), 1 )
        box.Add(wx.Button(panel, -1, 'Button2'), 1 )
        box.Add(wx.Button(panel, -1, 'Button3'), 1 )
        panel.SetSizer(box)
        self.Centre()


class MyApp(wx.App):
     def OnInit(self):
         frame = MyFrame(None, -1, 'wxboxsizer.py')
         frame.Show(True)
         return True


app = MyApp(0)
app.MainLoop()