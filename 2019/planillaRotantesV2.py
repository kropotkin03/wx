from wx import *
from wx.dataview import * 
import sqlite3
from sqlalchemy import *

class MiApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, "Movimiento de Rotantes", size=(700, 500))
        p1 = self.p1 = Panel(f1, -1 )
        self.dvlc = dvlc = DataViewListCtrl(p1)

        # Se crea los encabezados del frame
        dvlc.AppendTextColumn('#', width=30)
        dvlc.AppendTextColumn('Numero de Parte', width=130, mode=DATAVIEW_CELL_EDITABLE)# cell editable sirve para editar celdas
        dvlc.AppendTextColumn('Designacion', width=250, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('N/S', width=70, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Posicion', width=75, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('N° de desm.(SIL)', width=100, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('N° de mont(SIL)', width=40, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Estado', width=130, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Observ. de Desmontado', width=250, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('N/S Reemplazante', width=50, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('N°Desmontaje SIL reempl.', width=75, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('N°Montaje SIL reempl.', width=100, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Fecha de Montaje', width=75, mode=DATAVIEW_CELL_EDITABLE)
        dvlc.AppendTextColumn('Observ. de Montaje', width=75, mode=DATAVIEW_CELL_EDITABLE)

        hor = BoxSizer(HORIZONTAL)
        b = Button(p1, -1, "&Carga de Planilla de Aeronave")# se crea en el frame principal un boton para la carga de la planilla
        bA = Button(p1, -1, "&cargar elemento")# se crea un boton para la carga de un elemento en partucular que se agregara a la planilla
        #bB = Button(p1, -1, "&Borrar elemento") # se crea otro boton para el borrado del elemento
        hor.Add(b)
        hor.Add(bA)
        #hor.Add(bB)
        sizer = BoxSizer(VERTICAL)
        sizer.Add(dvlc, 1, EXPAND)
        b.Bind(EVT_BUTTON, self.cargaDatos)
        bA.Bind(EVT_BUTTON, self.addData)
        sizer.Add(hor)
        p1.SetSizer(sizer)
        f1.Show()


        dvlc.Bind(EVT_DATAVIEW_SELECTION_CHANGED, self.sele)
        dvlc.Bind(EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.OnValueChanged)
        
        return True


    
    def sele(self, evt):
        row = self.dvlc.GetSelectedRow()
        print(row)
        print("Nombre", self.dvlc.GetTextValue(row, 2))
        print("Comisión", self.dvlc.GetTextValue(row, 3))
    
# en esta funcion se realiza la modificacion de los campos
    def OnValueChanged(self, evt): 
        print("OnValueChanged")
        row = self.dvlc.GetSelectedRow()
        print(row)
        NumParte = self.dvlc.GetTextValue(row, 1)
        Designacion = self.dvlc.GetTextValue(row, 2)
        NumSerie = self.dvlc.GetTextValue(row, 3)
        Posicion = self.dvlc.GetTextValue(row, 4)
        NumDesmSIL= self.dvlc.GetTextValue(row, 5)
        NumMontSIL = self.dvlc.GetTextValue(row, 6)
        Estado = self.dvlc.GetTextValue(row, 7)
        ObserDesm = self.dvlc.GetTextValue(row, 8)
        NumSerieReempl = self.dvlc.GetTextValue(row, 9)
        NumDesmSILReempl = self.dvlc.GetTextValue(row, 10)
        NumMontSILReempl = self.dvlc.GetTextValue(row, 11)
        FechaMontaje = self.dvlc.GetTextValue(row, 12)
        ObservMont = self.dvlc.GetTextValue(row, 13)
        id = self.dvlc.GetTextValue(row, 0)
        self.grabaBD(id, NumParte, Designacion, NumSerie, Posicion, NumDesmSIL, NumMontSIL, Estado, ObserDesm, NumSerieReempl, NumDesmSILReempl, NumMontSILReempl, FechaMontaje, ObservMont)
        
        

    def cargaDatos(self, e):
        lista = self.recupBD()
        #print(lista)
        for e in lista:
            self.dvlc.AppendItem(e)

    def recupBD(self):
        con = sqlite3.connect("aeronaves.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM PampaE830 ORDER BY Designacion") # ordena la columna designacion alfabeticamente
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        for e in listaA:
            e[0] = str(e[0])
        con.close()
        return listaA

    def addData(self):
        # se crea una lista para luego poder recorrerla y crear los static text
        pass

        
        """ self.listaCampos = listaCampos = ['Numero de Parte','Designacion','N/S','Posicion','N° de desm.(SIL)',\
            'N° de mont(SIL)','Estado','Observ. de Desmontado','N/S Reemplazante','N° Montaje SIL reempl.','Fecha de Montaje','Observ. de Montado',] 
        self.listaValores = listaValores = [] # se guardara en una lista los valores cargados en cada uno de los campos
        f1 = Frame(None, size=(350,400), title="Carga de Elemeto Nuevo") # se crea el frame pincipal en donde se pondra los static y los textcrl
        gridBag = GridBagSizer(10, 10) # se crea una grilla en donde se colocara los static y textcrl
        boton = Button(f1,label="&cargar", ) # se crea un boton
    
        for i in range(len(listaCampos)): # se recorre en un for la lista de los campos
            campo = listaCampos[i] # se guardara en una variable cada unos de los campos de la lista
            staticCampo = StaticText(f1, label=campo) # se crea el static para cada vuelta del for
            gridBag.Add(staticCampo, pos=(i,0)) # se agrega al gridbadsizer el static
            tD = TextCtrl(f1) # se crea un textcrl 
            gridBag.Add(tD, pos=(i,2)) # se lo agrega   
            listaValores.append(tD) # se lo agrega a una lista      
            #gridBag.Add(dia, pos=(i+1,0))
        
        
        gridBag.Add(boton, pos=(9,1)) # se crea un boton 
        boton.Bind(EVT_BUTTON, self.calculoLiuvia) # se crea el evento que iniciara cuando se preciona enter o click en el boton
    

        
        f1.SetSizer(gridBag) # se muestra el grid en el frame
        f1.Show() """    # se muetra el frame
 
        
    """ def creaElemento():
        con = sqlite3.connect("aeronaves.db")
        cur = con.cursor()
        cur.execute("INSERT INTO PampaE830(NumParte, Designacion, NumSerie, Posicion, NumDesmSIL, NumMontSIL, Estado, ObserDesm, NumSerieReempl, NumDesmSILReempl, NumMontSILReempl, FechaMontaje, ObservMont) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", (NumParte, Designacion, NumSerie, Posicion, NumDesmSIL, NumMontSIL, Estado, ObserDesm, NumSerieReempl, NumDesmSILReempl, NumMontSILReempl, FechaMontaje, ObservMont)))

        con.commit()
        con.close()

        return True
 """    # en la siguiente fncion se mandan todos los campos que se desean guardar y 
    # que fueron modificados
    def grabaBD(self,id, pNumParte, pDesignacion, pNumSerie, pPosicion, pNumDesmSIL, pNumMontSIL, pEstado, pObserDesm,pNumSerieReempl, pNumDesmSILReempl, pNumMontSILReempl, pFechaMontaje, pObservMont):

        engine = create_engine('sqlite:///aeronaves.db')
        conn = engine.connect()
        metadata = MetaData()
        # se establecen todas las colunas que se desean guardar
        PampaE830 = Table('PampaE830', metadata, 
            Column('id', Integer(), primary_key=True),
            Column('NumParte', String(20)),
            Column('Designacion', String(50)),
            Column('NumSerie', String(20)),
            Column('Posicion', String(20)),
            Column('NumDesmSIL', String(20)),
            Column('NumMontSIL', String(20)),
            Column('Estado', String(20)),
            Column('ObserDesm', String(20)),
            Column('NumSerieReempl', String(20)),
            Column('NumDesmSILReempl', String(20)),
            Column('NumMontSILReempl', String(20)),
            Column('FechaMontaje', String(20)),
            Column('ObservMont', String(20))
        )

        t = conn.begin()

        s = update(PampaE830).where(
            PampaE830.c.id == id
        ).values(
        NumParte = pNumParte,
        Designacion = pDesignacion,
        NumSerie = pNumSerie,
        Posicion = pPosicion,
        NumDesmSIL = pNumDesmSIL,
        NumMontSIL = pNumMontSIL,
        Estado = pEstado,
        ObserDesm = pObserDesm,
        NumSerieReempl = pNumSerieReempl,
        NumDesmSILReempl = pNumDesmSILReempl,
        NumMontSILReempl = pNumMontSILReempl,
        FechaMontaje = pFechaMontaje,
        ObservMont = pObservMont
        )


        conn.execute(s) # se le mada la variable que previamente se creo
        t.commit()
                  

       

prog = MiApp()
prog.MainLoop()
