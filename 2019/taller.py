from wx import *
from wx.dataview import *
import sqlite3

class MyApp(App):
    def OnInit(self):
        f = Frame(None,-1,"Clientes",size = (900,500))
        p = Panel(f,-1)
        self.dvlc = dvlc = DataViewListCtrl(p)
        header = [('º',30), ('Nombre',150), ('Auto',150), ('Celular',150), ('Entregado',150),]
        dvlc.AppendTextColumn('°',width =30)
        dvlc.AppendTextColumn('Nombre',width =150)
        dvlc.AppendTextColumn('Apellido',width=150)
        dvlc.AppendTextColumn('Auto',width =150)
        dvlc.AppendTextColumn('Celular',width =150)
        dvlc.AppendTextColumn('Entregado',width =150)
        dvlc.AppendTextColumn('Saldo',width =100)
        bs = BoxSizer(HORIZONTAL)
        boton = Button(p,-1,"Cargar cliente")
        boton2 = Button(p,-1,"Borrar cliente")
        boton.Bind(EVT_BUTTON, self.add_client)
        bs.Add(boton)
        bs.Add(boton2)
        bs2 = BoxSizer(VERTICAL)
        bs2.Add(dvlc,-1,EXPAND)
        bs2.Add(bs)
        p.SetSizer(bs2)
        f.Show()
        return True

    def add_client(self, evt):
        f2 = Frame(None,-1,"Agregar cliente",size=(200,250))
        self.p2 = Panel(f2,-1)
        gb = GridBagSizer(5,5)
        #Nombre
        name_title = StaticText(self.p2,-1,"Nombre")
        gb.Add(name_title, pos=(0,0))
        self.name_control = TextCtrl(self.p2,-1)
        gb.Add(self.name_control,pos = (0,1))
        #Apellido 
        lname_title = StaticText(self.p2,-1,"Apellido")
        gb.Add(lname_title, pos=(1,0))
        self.lname_control = TextCtrl(self.p2,-1)
        gb.Add(self.lname_control, pos =(1,1))
        #Auto
        carbrand_title = StaticText(self.p2,-1,"Auto")
        gb.Add(carbrand_title, pos=(2,0))
        self.carbrand_control = TextCtrl(self.p2,-1)
        gb.Add(self.carbrand_control, pos=(2,1))
        #Celular
        mobileph_title = StaticText(self.p2,-1,"Celular")
        gb.Add(mobileph_title, pos=(3,0))
        self.mobileph_control = TextCtrl(self.p2,-1)
        gb.Add(self.mobileph_control, pos=(3,1))
        #Entregado
        e_title= StaticText(self.p2,-1,"Entregado")
        gb.Add(e_title, pos=(4,0))
        self.e_control = TextCtrl(self.p2,-1)
        gb.Add(self.e_control,pos=(4,1))
        #Saldo
        s_title= StaticText(self.p2,-1,"Saldo")
        gb.Add(s_title, pos=(5,0))
        self.s_control = TextCtrl(self.p2,-1)
        gb.Add(self.s_control,pos=(5,1))
        #Save
        save_button = Button(self.p2,-1,"Guardar")
        gb.Add(save_button,pos=(6,1))
        save_button.Bind(EVT_BUTTON,self.save)
        #Acomoda y Muestra
        self.p2.SetSizerAndFit(gb)
        f2.Show()

    def save(self,evt):
        ln = self.lname_control.GetValue()
        gn = self.name_control.GetValue()
        car = self.carbrand_control.GetValue()
        mph = self.mobileph_control.GetValue()
        ge = self.e_control.GetValue()
        gs = self.s_control.GetValue()
        print([gn,ln,car,mph,ge,gs])
        self.dvlc.AppendItem(["", gn,ln,car,mph,ge,gs])

app = MyApp()
app.MainLoop()
