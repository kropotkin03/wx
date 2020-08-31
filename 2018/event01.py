import wx
# create event class
import wx.lib.newevent

class MyApp(wx.App):
    def OnInit(self):
        f = wx.Frame(None, -1)
        SomeNewEvent, EVT_SOME_NEW_EVENT = wx.lib.newevent.NewEvent()
        wx.PostEvent(target, SomeNewEvent(attr1=foo, attr2=bar))
        target.Bind(EVT_SOME_NEW_EVENT, target.handler)
        f.Show()
        return True

app = MyApp()
app.MainLoop()