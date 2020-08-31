from wx import *


class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        s = BoxSizer(VERTICAL)
        b = Button(f, label="otro frame")
        b.Bind(EVT_BUTTON, self.otroFrame)
        s.Add(b, 0, ALL|EXPAND, 50)
        f.SetSizer(s)
        f.Show()
        return True

    def otroFrame(self, event):
        f2 = Frame(None, title="otro frame")
        


        f2.Show()

app = MyApp()
app.MainLoop()
