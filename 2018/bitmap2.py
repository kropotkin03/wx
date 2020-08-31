from wx import *

class MiApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Anikka Albrite", size = (500, 800))
        p1 = Panel(f, -1, size = (500, 400))
        p1.SetBackgroundColour('#ff0000')
        b = Button(p1, -1, label="", size = (160, 210))
        b.SetBitmap(BitmapFromImage(Image("anikka.jpg", BITMAP_TYPE_ANY).Rescale(150, 200))) # cambiar size
        b.Bind(EVT_BUTTON, self.click)
        p2 = Panel(f, -1)
        p2.SetBackgroundColour('#00ff00')
        self.texto = StaticText(p2, -1, "")
        g = BoxSizer(VERTICAL)
        g.Add(p1,0)
        g.Add(p2,0, EXPAND|ALL,border=10)
        f.SetSizer(g)
        f.Show(True)
        return True

    def click(self, event):
        self.texto.SetLabel("No hacerse los locos que es mi novia!!!!!!!")

app = MiApp()
app.MainLoop()