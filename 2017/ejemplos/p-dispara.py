from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None)
        vent = Panel(f, -1)
        self.entrada1 = TextCtrl(vent,-1,pos=(-100,-100),size=(10,10),value="")
        self.entrada1.Bind(EVT_CHAR, self.teclazo)

        f.Show()
        return True

    def teclazo(self, event):
        if event.GetKeyCode() != ord("p"):
            event.Skip()
        else:
            print "verga"

app = MiApp()
app.MainLoop()
