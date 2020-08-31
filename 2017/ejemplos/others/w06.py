from wx import *
from ej06 import *
from wx.lib.pubsub import pub


class Saludos(Ventana):
    def __init__(self):
        Ventana.__init__(self, None)
        self.b_cargar.Bind(EVT_BUTTON, self.hacer_carga)

    def hacer_carga(self, event):
        n = self.nombre.GetValue()
        pub.sendMessage("panelListener", message=n)

class MiVentana(Ventana2):
    def __init__(self):
        Ventana2.__init__(self, None)


class MiAplicacion(App):
    def OnInit(self):
        frame = Saludos()
        pub.subscribe(self.myListener, "panelListener")
        self.t = TextCtrl(frame, -1, "")
        frame.Show()
        self.f2 = MiVentana()
        self.f2.Show(False)

        return True


    def myListener(self, message):
        self.t.SetValue(message)


    def onOpenFrame(self, event):
        f2 = MiVentana()
        f2.Show()


app = MiAplicacion()
app.MainLoop()
