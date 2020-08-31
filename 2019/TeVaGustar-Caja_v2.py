from wx import *
from wx.dataview import *
from wx.adv import *
import sqlite3
from sqlalchemy import *
from datetime import date

class MyApp(App):
    def OnInit(self):
        f = Frame(None, title="Te va gustar-caja", size=(1100,600))
        p = self.p = Panel(f, -1)
        self.dvlc = dvlc = DataViewListCtrl(p)
        dvlc.AppendTextColumn('#', width=30)
        dvlc.AppendTextColumn('Apellido y nombres', width=250)
        dvlc.AppendTextColumn('Fecha', width=150)
        dvlc.AppendTextColumn('Entrega', width=100)
        dvlc.AppendTextColumn('Forma de pago', width=100)
        dvlc.AppendTextColumn('Retira', width=100)
        dvlc.AppendTextColumn('Saldo', width=100)
        dvlc.AppendTextColumn('Telefono', width=200)
        hor = BoxSizer(HORIZONTAL)
        b = Button(p, -1, "&Agregar persona")
        b2 = Button(p, -1, "Alta al sitema")
        hor.Add(b)
        hor.Add(b2)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.abrirAgP)
        sizer.Add(hor)
        p.SetSizer(sizer)
        lista = self.recupBD()
        
        for e in lista:
            self.dvlc.AppendItem(e)        
        f.Show()
        dvlc.Bind(EVT_DATAVIEW_SELECTION_CHANGED, self.sele)
        return True

    def sele(self, e):
        self.abrirAgP(e)




    def recupBD(self):
        con = sqlite3.connect("caja.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM datos ORDER BY nombre")
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        for e in listaA:
            e[0] = str(e[0])
            e[3] = str(e[3])
            e[5] = str(e[5])
            e[6] = str(e[6])
        con.close()
        return listaA

    def abrirAgP(self, e):
        f2 = Frame(None, -1, "Agregar persona", size = (350, 300))
        p2 = self.p2 = Panel(f2, -1, style = TAB_TRAVERSAL)
        grilla = GridBagSizer(5,5)

# Nombre - Caja de Texto
        l_nom = StaticText(p2, -1, "Apellido y nombres")
        grilla.Add(l_nom, pos = (0,0))
        nom = self.nom =TextCtrl(p2, -1)
        grilla.Add(nom, pos = (0,1), span = (1, 3))
# Fecha - Caja de Texto con fecha de hoy - Abre datepicker
        l_fna = StaticText(p2, -1, "Fecha")
        grilla.Add(l_fna, pos = (1,0))
        self.fe = date.today().isoformat()
        fna =self.fna = DatePickerCtrl(p2, size=(120, -1), style= DP_DROPDOWN | DP_SHOWCENTURY)
        fna.Bind(EVT_DATE_CHANGED, self.OnDateChanged, fna) # este evento es para cuando NO ES BOTON
        grilla.Add(self.fna, pos = (1,1), span = (1, 3))
# Entrega - Caja de texto
        l_ent = StaticText(p2, -1, "Entrega")
        grilla.Add(l_ent, pos = (2,0))
        ent = self.ent =TextCtrl(p2, -1)
        grilla.Add(ent, pos = (2,1), span = (1, 3))
# Forma de pago - Combo
        l_fpag = StaticText(p2, -1, "Forma de pago")
        grilla.Add(l_fpag, pos = (3,0))
        fpagList = ["Efectivo", "Tarjeta debito", "Tarjeta credito", "Solo retira"]
        self.fpag = cb = ComboBox(p2, 500, "Forma de pago", (0, 0), (160, -1), fpagList, CB_DROPDOWN | TE_PROCESS_ENTER )
        cb.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        grilla.Add(self.fpag, pos = (3,1), span = (1, 3))
# Retira - Caja de texto
        l_ret = StaticText(p2, -1, "Retira")
        grilla.Add(l_ret, pos = (4,0))
        ret = self.ret = TextCtrl(p2, -1)
        grilla.Add(ret, pos=(4,1), span = (1, 3))
# Saldo - Caja de Texto
        l_sal = StaticText(p2, -1, "Saldo")
        grilla.Add(l_sal, pos=(5,0))
        sal = self.sal = TextCtrl(p2, -1)
        grilla.Add(sal, pos=(5,1), span = (1, 3))
# Telefono - Caja de Texto
        l_tel = StaticText(p2, -1, "Telefono")
        grilla.Add(l_tel, pos=(6,0))
        tel = self.tel = TextCtrl(p2, -1)
        grilla.Add(tel, pos=(6,1), span = (1, 3))
# Botón Guardar
        guardar = Button(p2, -1, "&Guardar")
        grilla.Add(guardar, pos = (7, 0))
        guardar.Bind(EVT_BUTTON, self.guardaPart)

# Muestra la grilla
        p2.SetSizerAndFit(grilla)
        f2.Show()

#Guarda el participante
    def guardaPart(self, evt):
        no = self.nom.GetValue()
        fn = self.fna.GetValue()
        en = self.ent.GetValue()
        fp = self.fp = self.fpag.GetValue()
        re = self.ret.GetValue()
        sa = self.sal.GetValue()
        te = self.tel.GetValue()
        self.dvlc.AppendItem(["0", no, self.fe, en, fp, re, sa, te]) 
        print(self.fe)       
        self.grabaBD(no, self.fe, en, fp, re, sa, te)
# Begin Combo
    def OnKillFocus(self, evt):
        self.fp = self.fpag.GetValue()
        evt.Skip()
# End Combo

# Begin Calendario
    def OnDateChanged(self, evt):
        print("OnDateChanged: %s\n" % evt.GetDate())
        d = evt.GetDate()
        print(d.FormatISODate())
        self.fe = d.FormatISODate()
        print("->", self.fe, "<-")
# End Calendario
    def grabaBD(self, pnombre, pfecha, pentrega, pformadepago, pretira, psaldo, ptelefono):
        
        engine = create_engine('sqlite:///caja.db')
        conn = engine.connect()
        metadata = MetaData()

        datos = Table('datos', metadata, 
                Column('id', Integer(), primary_key=True),
                Column('nombre', String(50)),
                Column('fecha', String(50)),
                Column('entrega', Integer()),
                Column('formadepago', String(20)),
                Column('retira', Integer()),
                Column('saldo', Integer()),
                Column('telefono', String(50))
        )

        t = conn.begin()
        ins = datos.insert().values(
                nombre = pnombre,
                fecha = pfecha,
                entrega = pentrega,
                formadepago = pformadepago,
                retira = pretira,
                saldo = psaldo,
                telefono = ptelefono
        )

        conn.execute(ins) 
        t.commit()
                
    def calculoSaldo(self, evt):
        pass



app = MyApp()
app.MainLoop()
