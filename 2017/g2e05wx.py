from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        self.bSh = BoxSizer(HORIZONTAL)
        self.bSvS = BoxSizer(VERTICAL)
        self.bSvT = BoxSizer(VERTICAL)
        self.bSh.Add(self.bSvS)
        self.bSh.Add(self.bSvT)
        self.mas = True
        self.texto = StaticText(f)

        self.s = TextCtrl(f, -1, "")
        self.bSvS.Add(self.s)
        self.s.Bind(EVT_CHAR, self.teclazo)

        f.SetSizer(self.bSh)
        f.Show()
        return True


    def teclazo(self, event):

        if 48 <= event.GetKeyCode() <= 57:
            event.Skip()
        #elif event.GetKeyCode() == 13:
         #   self.texto.SetLabel(self.s.GetValue())
          #  self.bSvT.Add(self.texto)

        else:
            self.texto.SetLabel(self.s.GetValue())
            self.bSvT.Add(self.texto)


a = MyApp()
a.MainLoop()
