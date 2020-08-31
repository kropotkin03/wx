from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "")
        p = Panel(f, -1)
        theButton = self.b =Button(p, 1000, "", pos = (100, 10))
        theButton.Bind(EVT_BUTTON, self.onClick)
        cantidad = 90 # si ponen 30 o mas se ejecuta el onClick, lo mismo que apretar el boton
        if cantidad >=30:
            evt = CommandEvent(EVT_BUTTON.typeId)
            evt.SetEventObject(theButton)
            evt.SetId(theButton.GetId())
            theButton.GetEventHandler().ProcessEvent(evt)

        f.Show()
        return True

    def onClick(self, e):
        print "cantidad vale mas de 30"
        print self.b.GetId()

app = MyApp()
app.MainLoop()

