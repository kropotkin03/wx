# -*- coding: utf-8 -*-
from wx import *

class MiApp(App):

    @property
    def OnInit(self):
        vent = Frame(None, title = "Rename")
        panel = Panel(vent)
        sizer = GridBagSizer(4, 4)

        text = StaticText(panel, label="Rename To")
        sizer.Add(text, pos=(0, 0), flag=TOP|LEFT|BOTTOM, border=5)

        tc = TextCtrl(panel)
        sizer.Add(tc, pos=(1, 0), span=(1, 5), flag=EXPAND|LEFT|RIGHT, border=5)

        buttonOk = Button(panel, label="Ok", size=(90, 28))
        buttonClose = Button(panel, label="Close", size=(90, 28))
        sizer.Add(buttonOk, pos=(3, 3))
        sizer.Add(buttonClose, pos=(3, 4), flag=RIGHT|BOTTOM, border=5)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)
        vent.Show()
        return True

app = MiApp()
app.MainLoop()