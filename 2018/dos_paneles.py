import wx


class MyApp(wx.App):
     def OnInit(self):

         frame = wx.Frame(None, -1, 'frame', size=(250, 250))
         panel1 = wx.Panel(frame, -1)
         panel1.SetBackgroundColour('#ff0000')
         button1 = wx.Button(panel1, -1, label="click me")

         panel2 = wx.Panel(frame, -1)
         panel2.SetBackgroundColour('#00ff00')
         button2 = wx.Button(panel2, -1, label="click me")
         sizer = wx.BoxSizer(wx.VERTICAL)
         sizer.Add(panel1,0,wx.EXPAND|wx.ALL,border=10)
         sizer.Add(panel2,0,wx.EXPAND|wx.ALL,border=10)

         frame.SetSizer(sizer)
         frame.Show(True)
         return True

app = MyApp(0)
app.MainLoop()