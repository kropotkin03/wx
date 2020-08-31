from wx import * 
from wx.dataview import *
import sqlite3

class Clientes(App):
    def OnInit(self):
#Frame1
        fr1=Frame(None,-1,"KtStudios(Estudio Palandri)",size=(1500,1200))
        p1=self.p1=Panel(fr1,-1)
        self.dvlc = dvlc = DataViewListCtrl(p1)
        cLientes=[("Hora y Fecha de cargado",150),("Cliente",150),("Empresa",150),("DNI",150),("CUIT",150),("Datos",150),("Honorarios",150)]
        for clt in cLientes:
            dvlc.AppendTextColumn(clt[0], width=clt[1])
        vHor=BoxSizer(HORIZONTAL)
        bot1=Button(p1,-1,"&Ingresar")
        vHor.Add(bot1)
        bot1.Bind(EVT_BUTTON,self.carga)
        bot3=Button(p1,-1,"Ingresar &Claves")
        vHor.Add(bot3)
        bot3.Bind(EVT_BUTTON,self.ingClave)
        bot4=Button(p1,-1,"&Ver Claves")
        vHor.Add(bot4)
        bot5=Button(p1,-1,"&Editar")
        vHor.Add(bot5)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        sizer.Add(vHor)
        p1.SetSizer(sizer)
        fr1.Show()
        dvlc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.ingClave)
        return True
    
#Frame 2
    def carga(self,event):
        fr2=Frame(None,-1,"Carga de datos",size=(350,450))
        p2=self.p2=Panel(fr2)
        grilla=GridBagSizer(5,5)
#Load Client
        clst=StaticText(p2,-1,"Cliente")
        grilla.Add(clst, pos=(2,1))
        wrtclst=self.wrtclst=TextCtrl(p2,-1,"")
        grilla.Add(wrtclst, pos=(2,2))
#Load Company
        comp=StaticText(p2,-1,"Compania")
        grilla.Add(comp, pos=(3,1))
        wrtcomp=self.wrtcomp=TextCtrl(p2,-1,"")
        grilla.Add(wrtcomp, pos=(3,2))
#Load DNI
        dNi=StaticText(p2,-1,"DNI")
        grilla.Add(dNi, pos=(4,1))
        wrtdNi=self.wrtdNi=TextCtrl(p2,-1,"")
        grilla.Add(wrtdNi, pos=(4,2))
        
#Load CUIT
        cuit=StaticText(p2,-1,"Cuit")
        grilla.Add(cuit, pos=(5,1))
        wrtcuit=self.wrtcuit=TextCtrl(p2,-1,"")
        grilla.Add(wrtcuit, pos=(5,2))
#Load Information 
        inFo=StaticText(p2,-1,"Informacion//Datos")
        grilla.Add(inFo, pos=(6,1))
        wrtinFo=self.wrtinFo=TextCtrl(p2,-1,"")
        grilla.Add(wrtinFo, pos=(6,2))
##Load Fee(Honorarios)
    #def cargaFee(self,event):
        fee=StaticText(p2,-1,"honorarios")
        grilla.Add(fee, pos=(7,1))
        wrtfee=self.wrtclav=TextCtrl(p2,-1,"")
        grilla.Add(wrtfee, pos=(7,2))
#Button for load in Frame 1
        grilla2=GridBagSizer(5,5)
        vhor=BoxSizer(VERTICAL)
        bot2=Button(p2,-1,"&Cargar")
        grilla.Add(bot2, pos=(8,1))
        vhor.Add(bot2)
        bot2.Bind(EVT_BUTTON,self.muesTra)
#Load Fecha
        l_fna = StaticText(p2, -1, "Registración")
        grilla.Add(l_fna, pos = (1,1))
        hoy = str(DateTime.Now())
       # hoy = hoy[3:5] + "/" + hoy[:2] + "/19" + hoy[6:8]
        fna =self.fna = TextCtrl(p2, -1, hoy)
        fna.SetLabel(str(DateTime.Now()))
        fna.SetEditable(False)
        self.fna.Bind(EVT_LEFT_DOWN, self.abrirCal) # este evento es para cuando NO ES BOTON
        grilla.Add(self.fna, pos = (1,2))

#Show grilla2
        p2.SetSizer(grilla)
        fr2.Show()

#Frame 3
    def ingClave(self,event):
        fr3=Frame(None,-1,"Registro De Claves",size=(300,350))
        p3=self.p3=Panel(fr3)
        grilla3=GridBagSizer(5,5)
#Load Clave Afip
        afiP=StaticText(p3,-1,"Afip")
        grilla3.Add(afiP, pos=(1,1))
        wrtafip=self.wrtafip=TextCtrl(p3,-1,"")
        grilla3.Add(wrtafip, pos=(1,2))
#Load Clave Gremio
        grem=StaticText(p3,-1,"Gremio")
        grilla3.Add(grem, pos=(2,1))
        wrtgrem=self.wrtgrem=TextCtrl(p3,-1,"")
        grilla3.Add(wrtgrem, pos=(2,2))
#Load Clave Cdi
        cdi=StaticText(p3,-1,"Ciudadano Digital")
        grilla3.Add(cdi, pos=(3,1))
        wrtcdi=self.wrtcdi=TextCtrl(p3,-1,"")
        grilla3.Add(wrtcdi, pos=(3,2))
#Load Clave Banco
        banco=StaticText(p3,-1,"Home Banking")
        grilla3.Add(banco, pos=(4,1))
        wrtbanco=self.wrtbanco=TextCtrl(p3,-1,"")
        grilla3.Add(wrtbanco, pos=(4,2))
#Load Clave Arba
        arba=StaticText(p3,-1,"Arba")
        grilla3.Add(arba, pos=(5,1))
        wrtarba=self.wrtarba=TextCtrl(p3,-1,"")
        grilla3.Add(wrtarba, pos=(5,2))
#Load Clave Ministerio  
        minis=StaticText(p3,-1,"Ministerio de trabajo")
        grilla3.Add(minis, pos=(6,1))
        wrtminis=self.wrtminis=TextCtrl(p3,-1,"")
        grilla3.Add(wrtminis, pos=(6,2))
#Button for load in Frame 1 from frame3
        bot5=Button(p3,-1,"&Cargar")
        grilla3.Add(bot5, pos=(7,1))
        
       # bot5.Bind(EVT_BUTTON,self.muesTra2)
#Show grilla3
        p3.SetSizer(grilla3)
        fr3.Show()
#Load in Frame 1
    def muesTra(self,event):
        self.lista=lista=[]
        wrtclst=self.wrtclst.GetValue()
        wrtcomp=self.wrtcomp.GetValue()
        wrtdNi=self.wrtdNi.GetValue()
        wrtcuit=self.wrtcuit.GetValue()
        wrtinFo=self.wrtinFo.GetValue()
        wrtfee=self.wrtclav.GetValue()
        fna =self.fna.GetValue() 
        self.dvlc. AppendItem([fna,wrtclst,wrtcomp,wrtdNi,wrtcuit, wrtinFo,wrtfee])
        lista=[fna,wrtclst,wrtcomp,wrtdNi,wrtcuit, wrtinFo,wrtfee]
        self.cargaClienteSql(lista)
# Begin Combo
    def OnKillFocus(self, evt):
        self.pr = self.pro.GetValue()
        evt.Skip()

#Cal
    def abrirCal(self,e):
        self.f3 = Frame(None, -1, "Día y Hora")
        g3 = BoxSizer()
        cal = CalendarCtrl(self.f3, -1, DateTime.Now())
        g3.Add(cal)
        cal.Bind(EVT_CALENDAR, self.OnCalSelected)
        self.f3.SetSizerAndFit(g3)
        self.f3.Show()

    def OnCalSelected(self, event):
        #print('OnCalSelected: %s\n' % e.GetDate())

        self.f3.Show(False)

    def cargaClienteSql(self,lista):
        con = sqlite3.connect("estudio.db")
        cur = con.cursor()
        print(lista)
        print(len(lista))

        try:
            cur.execute("CREATE TABLE personas (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, fecha NVARCHAR, cliente NVARCHAR, empresa NVARCHAR, dni NVARCHAR, cuit NVARCHAR, datos NVARCHAR,            honorarios NVARCHAR)")
        except:
            pass
        cur.execute("INSERT INTO personas(fecha,cliente,empresa,dni,cuit,datos,honorarios) VALUES (?,?,?,?,?,?,?)", lista,)
        con.commit()
        con.close()
app=Clientes()
app.MainLoop()
