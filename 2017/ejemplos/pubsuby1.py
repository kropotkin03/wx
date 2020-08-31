from wx import *
from wx.lib.pubsub import pub


class OtherFrame(Frame):
    def __init__(self):
        Frame.__init__(self, None)
        self.msgTxt = TextCtrl(self, value="")
        closeBtn = Button(self, label="Send and Close")
        closeBtn.Bind(EVT_BUTTON, self.onSendAndClose)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(self.msgTxt)
        sizer.Add(closeBtn)
        self.SetSizer(sizer)

    def onSendAndClose(self, event):
        msg = self.msgTxt.GetValue()
        pub.sendMessage("panelListener", message=msg)
        self.Close()


class MyApp(App):
    def OnInit(self):
        frame = Frame(None)
        pub.subscribe(self.myListener, "panelListener")
        cartel = StaticText(frame, -1, "Hacer click para abrir otro frame donde cargamos datos en este listbox")
        btn = Button(frame, label="Open Frame")
        self.t = ListBox(frame, -1)
        s = BoxSizer(VERTICAL)
        s.Add(cartel)
        s.Add(btn)
        s.Add(self.t)
        frame.SetSizer(s)
        btn.Bind(EVT_BUTTON, self.onOpenFrame)
        frame.Show()
        return True

    def myListener(self, message):
        self.t.Append(message)

    def onOpenFrame(self, event):
        f2 = OtherFrame()
        f2.Show()


app = MyApp()
app.MainLoop()
