from wx import *

a = App()
f = Frame(None)
text = StaticText(f, -1, 'pa darle gracia al texto')
colorete = (255, 0, 0)
text.SetForegroundColour(colorete)
fuente = Font(30, DECORATIVE, SLANT, BOLD)
text.SetFont(fuente)
f.Show()
a.MainLoop()
