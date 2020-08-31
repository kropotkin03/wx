import wx

class App (wx.App):
    def OnInit(self):
        self.lista=[]

        ventana =  wx.Frame (None, -1 , " Ejercicio 5 guia 1 " , size = (400,200))
        ventana.Center(True)
        caja = wx.BoxSizer (wx.VERTICAL)
        self.entrada01 = entrada01  = wx.TextCtrl (ventana)
        self.boton01   = boton01    = wx.Button   (ventana,-1,"Agregar")
        self.boton02   = boton02    = wx.Button   (ventana, -1, "Obtener total")

        caja.Add(entrada01)

        caja.Add(boton01)
        caja.Add(boton02)

        boton01.Bind (wx.EVT_BUTTON,self.Agregar)
        boton02.Bind (wx.EVT_BUTTON, self.Total)

        self.s = wx.StaticText(ventana,-1,label  = " Resultado ")
        caja.Add(self.s)

        ventana.SetSizer(caja)
        ventana.Show()
        return True
    def Agregar(self,event):
        n1 =int( self.entrada01.GetValue())
        self.lista.append(n1)
    def Total(self,event):
        i=0
        for x in range (len (self.lista)):
            i = i + self.lista[x]
        i = str(i)
        self.s.SetLabel(i)

#C:\Users\Ismael\PycharmProjects\untitled

App = App ()

App.MainLoop()