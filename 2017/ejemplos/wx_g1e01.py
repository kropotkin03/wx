# -*- coding:utf8 -*-
from wx import *

class Sumita(Frame):
    def __init__(self,parent,id,title):
        Frame.__init__(self,parent,id,title)
        grilla = GridSizer(3,3,5,5)
        self.entrada1 = TextCtrl(self,-1,value="")
        grilla.Add(self.entrada1,0,0)
        self.entrada2 = TextCtrl(self,-1,value="")
        grilla.Add(self.entrada2,0,1)
        boton = Button(self,-1,label="Suma")
        grilla.Add(boton, 1,0)
        boton.Bind (EVT_BUTTON, self.CliqueaBoton)
        self.etiqueta = StaticText(self,-1,label=u'')
        grilla.Add(self.etiqueta, 1,1 )
        self.SetSizer(grilla)
        self.Fit()
        self.Show(True)

    def CliqueaBoton(self, event):
        n1 = int(self.entrada1.GetValue())
        n2 = int(self.entrada2.GetValue())
        salida = n1 + n2
        salida = "La suma es: " + str(salida)
        self.etiqueta.SetLabel(salida)

app = App()
sumar = Sumita(None,-1,'Sumar')
app.MainLoop()