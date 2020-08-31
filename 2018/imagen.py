from wx import *


class MyApp(App):
    def OnInit(self):
        f = Frame(None, size=(500,600))
        p = Panel(f)
        box = BoxSizer(HORIZONTAL)
        descri = StaticText(p, -1, "descripcion del articulo bla bla bla bla bla bla")
        mapaDEbits = Image('anikka.jpg', BITMAP_TYPE_ANY) # el ANY es pa cualquier formato
        imagen = StaticBitmap(p, -1, Bitmap(mapaDEbits)) # no tenia tornillos para poner
        box.Add(descri, 0, ALL, 30)
        box.Add(imagen, 0, ALL, 30)
        p.SetSizer(box)
        f.Show()
        return True



a = MyApp()
a.MainLoop()



