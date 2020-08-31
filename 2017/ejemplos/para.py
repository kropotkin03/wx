from functools import partial
import wx


class DemoFrame(wx.Frame):
    """ This window displays a set of buttons """

    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        sizer = wx.BoxSizer(wx.VERTICAL)
        for button_name in ["first", "second", "third"]:
            btn = wx.Button(self, label=button_name)
            btn.Bind(wx.EVT_BUTTON, partial(self.OnButton, button_label=button_name))
            sizer.Add(btn, 0, wx.ALL, 10)

        self.SetSizerAndFit(sizer)

    def OnButton(self, Event, button_label):
        print "In OnButton:", button_label


app = wx.App(False)
frame = DemoFrame(None, title="functools.partial Bind Test")
frame.Show()
app.MainLoop()