import wx
from wx.lib.pubsub import pub


########################################################################
class OtherFrame(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY, "Secondary Frame")
        panel = wx.Panel(self)

        msg = "Enter a Message to send to the main frame"
        instructions = wx.StaticText(panel, label=msg)
        self.msgTxt = wx.TextCtrl(panel, value="")
        closeBtn = wx.Button(panel, label="Send and Close")
        closeBtn.Bind(wx.EVT_BUTTON, self.onSendAndClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        flags = wx.ALL | wx.CENTER
        sizer.Add(instructions, 0, flags, 5)
        sizer.Add(self.msgTxt, 0, flags, 5)
        sizer.Add(closeBtn, 0, flags, 5)
        panel.SetSizer(sizer)

    # ----------------------------------------------------------------------
    def onSendAndClose(self, event):
        """
        Send a message and close frame
        """
        msg = self.msgTxt.GetValue()
        pub.sendMessage("panelListener", message=msg)
        #pub.sendMessage("panelListener", message="test2", arg2="2nd argument!")
        self.Close()


########################################################################
class MyPanel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        pub.subscribe(self.myListener, "panelListener")

        btn = wx.Button(self, label="Open Frame")
        self.t = wx.TextCtrl(self, -1)
        s = wx.BoxSizer()
        s.Add(btn)
        s.Add(self.t)
        self.SetSizer(s)
        btn.Bind(wx.EVT_BUTTON, self.onOpenFrame)

    # ----------------------------------------------------------------------
    def myListener(self, message, arg2=None):
        """
        Listener function
        """

        self.t.SetValue(message)

    # ----------------------------------------------------------------------
    def onOpenFrame(self, event):
        """
        Opens secondary frame
        """
        frame = OtherFrame()
        frame.Show()


########################################################################
class MyFrame(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="New PubSub API Tutorial")
        panel = MyPanel(self)
        self.Show()

app = wx.App(False)
frame = MyFrame()
app.MainLoop()
