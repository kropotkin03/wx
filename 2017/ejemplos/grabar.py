from wx import *

class A(App):
    def OnInit(self):
        f = Frame(None)
        b = Button(f, -1, "Guardarrrrrrrr")
        b.Bind(EVT_BUTTON, self.guardar)
        f.Show()
        return True


    def guardar(self, event):
        dlg = wx.FileDialog(None, "Guardar archivo ...", "", "", style=FD_SAVE)
        dlg.ShowModal()
        dlg.Destroy()

a = A()
a.MainLoop()
