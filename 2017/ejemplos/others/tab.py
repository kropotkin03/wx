import  wx

class MiApp(wx.App):

    def OnInit(self):
        frame = wx.Frame(None, -1, "")
        panel = wx.Panel(frame, -1)
        t1 = wx.TextCtrl(panel, -1, "Test it out and see", size=(125, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, t1)
        t1.Bind(wx.EVT_CHAR, self.EvtChar)
        t2 = wx.TextCtrl(panel, -1, "", size=(125, -1), style=wx.TE_PASSWORD)
        self.Bind(wx.EVT_TEXT, self.EvtText, t2)
        frame.Show()
        return True

    def EvtChar(self, event):
        event.Skip()
    def EvtText(self, event):
        self.log.WriteText('EvtText: %s\n' % event.GetString())

    def EvtTextEnter(self, event):
        self.log.WriteText('EvtTextEnter\n')
        event.Skip()


win = MiApp()
win.MainLoop()
#---------------------------------------------------------------------------
