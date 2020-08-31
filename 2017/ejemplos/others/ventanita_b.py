from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None)
        panel = Panel(f, -1)
        button = Button(panel, 1003, "Cerrame")
        button.Bind(EVT_BUTTON, self.OnCloseMe, button)
        button.Bind(EVT_CLOSE, self.OnCloseWindow)
        f.Show()
        return True


    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()


app = MiApp()
app.MainLoop()
