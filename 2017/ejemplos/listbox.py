from wx import *
import time

class MiApp(App):
    def OnInit(self):
        f = Frame(None, -1, pos = (0,0), size = (200, 300))
        d = ["pepe", "luis", "ana", "jajajajaja"]
        self.lista = ListBox(f, -1, DefaultPosition, DefaultSize, d)
        self.b = Button(f, -1, pos=(140,0))

        self.b.Bind(EVT_BUTTON, self.borrar)
        self.b.Bind(EVT_ENTER_WINDOW, self.mouseSobre)
        f.Show()

        return True


    def mouseSobre(self, event):
        # mouseover changes colour of button
        time.sleep(5)
        self.b.SetBackgroundColour('Green')
        event.Skip()


    def borrar(self, e):
        for i in self.lista.GetSelections():
            print i
            self.lista.Delete(i)

a = MiApp()
a.MainLoop()
