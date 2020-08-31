from wx import *


class MyApp(App):
    def OnInit(self):
        self.ventana = frame = Frame(None)
        sizer = BoxSizer(VERTICAL)
        frame.SetSizer(sizer)

        bCerrar = Button(frame, label="Cerrar")
        bCerrar.Bind(EVT_BUTTON, self.onClose)
        sizer.Add(bCerrar, 0, ALL, 50)

        frame.Show()
        return True
        
    def onClose(self, evt):
        self.ventana.Close()


app = MyApp()
app.MainLoop()