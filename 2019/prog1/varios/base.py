from wx import *


class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(-1, 500))
        s = BoxSizer(VERTICAL)
        t = TextCtrl(f)
        s.Add(t, 0, ALL|EXPAND, 50)
        b = Button(f, label="botoncito", style=BORDER_NONE)
        b.SetBackgroundColour((0,0,255))
        s.Add(b, 0, ALL|EXPAND, 50)
        f.SetSizer(s)
        f.Show()
        return True


app = MyApp()
app.MainLoop()
