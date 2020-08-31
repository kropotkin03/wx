from wx  import *
from validador import *


app = App()
f = Frame(None)
t = TextCtrl(f, validator=MyValidator())
f.Show()
app.MainLoop()
