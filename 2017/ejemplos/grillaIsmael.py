# -*- coding:utf8 -*-
from wx import *


class MyApp(App):
    def OnInit(self):
        mainFrame = Frame(None)
        mainFrame.SetBackgroundColour("blue")
        mainSz = BoxSizer(HORIZONTAL)
        pLeft = Panel(mainFrame, size = (50, 221))
        pLeft.SetBackgroundColour("green")
        riteSz = BoxSizer(VERTICAL)
        mainSz.Add(pLeft, 0, EXPAND)
        mainSz.Add(riteSz, 6, EXPAND)
        pUp = Panel(mainFrame, size = (-1, 30))
        pUp.SetBackgroundColour("red")
        riteSz.Add(pUp, 0, EXPAND)
        grilla = GridBagSizer(20, 20)
        for x in range(5):
            bn = Button(mainFrame)
            bn.SetLabel("Botoncin" + str(x))
            grilla.Add(bn , (x,x), flag=EXPAND )
        riteSz.Add(grilla, 7, EXPAND)
        mainFrame.SetSizer(mainSz)
        mainFrame.Show()
        return True


app = MyApp()
app.MainLoop()

