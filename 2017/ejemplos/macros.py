# -*- coding:utf8 -*-
from wx import *

class MyApp(App):
    def OnInit(self):
        mainFrame = Frame(None)



        mainFrame.Show()
        return True

app = MyApp()
app.MainLoop()

