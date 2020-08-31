# -*- coding:utf8 -*-
from wx import *

class MiApp(App):
    def OnInit(self):
        vent = Frame(None, -1, "g1e01", size = (500, 500))
        self.etiqueta1 = wx.StaticText(vent,-1,label='Ingrese nombre:', pos = (0,0))
        self.entrada1 = TextCtrl(vent,-1,value="", pos = (100,0))
        self.etiqueta2 = wx.StaticText(vent,-1,label='Ingrese sexo:', pos = (0,40))
        self.etiqueta3 = wx.StaticText(vent,-1,label='', pos = (100,300))
        radio1 = RadioButton(vent, -1, "Femenino", pos = (100,40),style=wx.RB_GROUP)
        radio2 = RadioButton(vent, -1, "Masculino", pos = (200,40))
        for eachRadio in [radio1, radio2]:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, eachRadio)

        boton = Button(vent,-1,label="Ejecutar", pos = (0,80))

        boton.Bind (EVT_BUTTON, self.CliqueaBoton)
        self.etiqueta = StaticText(vent,-1,label=u'')
        #vent.Fit()
        vent.Show(True)
        return True

    def OnRadio(self, event):
        radioSelected = event.GetEventObject()
        text = radioSelected.GetLabel()
        self.selectedText = text

    def CliqueaBoton(self,event):
        self.etiqueta3.SetLabel(self.entrada1.GetValue() + " es " + self.selectedText)

app = MiApp()
app.MainLoop()
