from wx import *
from wx.dataview import *
import sqlite3

class MyApp(App):
    def OnInit(self):
        self.listaTotal = []
        self.v = v = Frame( None, title = "Vapeo", size = (500, 600))
        self.dvlc = DataViewListCtrl(v)
        encabezado = [['Líquidos', 100], ('Stock', 100), ('Tipo', 100), ("Subtipo", 100), ("Nicotina %", 100)]
        for enca in encabezado:
            self.dvlc.AppendTextColumn(enca[0], width = enca[1])
        self.boxs = boxs = BoxSizer(HORIZONTAL)
        self.dvlc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.editar)
        boton = Button(v, label = "Ingresar líquido")
        boton.Bind(EVT_BUTTON, self.liquidos)
        boxs.Add(boton)
        boton2 = Button(v, label = "Borrar")
        boton2.Bind(EVT_BUTTON, self.borrar)
        boxs.Add(boton2)
        self.sizer = sizer = BoxSizer(VERTICAL)
        sizer.Add(self.dvlc, -1, EXPAND)
        sizer.Add(boxs)

        v.SetSizer(sizer)
        self.mostrarClientes()
        v.Show()
        return True

       
        
    def liquidos (self, event):
        self.v2 = v2 = Frame(None, title = "Ingresar el líquido")
        self.gbs = gbs = GridBagSizer(10,10)
        t1 = StaticText(v2, label = "Nombre")
        gbs.Add(t1, pos = (1,1))
        self.nom = nom = TextCtrl(v2)
        gbs.Add (nom, pos = (1,2))
        t2 = StaticText(v2, label = "Cantidad")
        gbs.Add(t2, pos = (2,1))
        elegir = []
        for i in range (11):
            n = str(i)
            elegir.append(n)
        elegir.append("más")
        self.stock = ComboBox(v2, value = "Elegir", choices = elegir, size = (100,35))
        gbs.Add(self.stock, pos = (2,2))
        self.masstock = TextCtrl(v2, value = "Ingresar cantidad", size = (130,35), validator = MyValidator())
        gbs.Add(self.masstock, pos = (2,3))
        t3 = StaticText(v2, label = "Tipo")
        cblist = ["Tabaqui", "Frutal", "Otro"]
        self.cb = ComboBox(v2, value = "Elegir", choices = cblist, size = (100,35))
        gbs.Add(self.cb, pos = (3,2))
        gbs.Add(t3, pos = (3,1))
        t4 = StaticText(v2, label = "Subtipo")
        gbs.Add(t4, pos = (4,1))
        self.subtipo = ComboBox (v2, value = "Ninguno", choices = ["Rubio", "Negro", "Otro"], size = (100,35))
        gbs.Add(self.subtipo, pos = (4,2))
        self.subtipoB = TextCtrl(v2, value = "Ingresar", size = (100,35))
        gbs.Add(self.subtipoB, pos = (4,3))
        t5 = StaticText(v2, label = "Nicotina")
        gbs.Add(t5, pos = (5,1))
        self.nico = ComboBox(v2, value = "0", choices = ["3","6"], size = (100,35))
        gbs.Add(self.nico, pos = (5,2))
        self.agr = agr = Button(v2, label = "&Agregar")
        gbs.Add(agr, pos = (6,1))
        agr.Bind(EVT_BUTTON, self.agregar)
        self.liquidosT = []
        self.liquidosS = []
        self.liquidosT.append(self.nom)
        self.liquidosS.append(self.stock)
        self.agr.Bind(EVT_BUTTON, self.agregar)
        self.cbN = TextCtrl(v2, value = "Ingrese el tipo", size = (110,35))
        self.gbs.Add(self.cbN, pos = (3,3))



        v2.SetSizerAndFit(gbs)
        v2.Show()    

    def agregar (self, event):
        self.list = []
        self.listaT = []
        self.subtipoT = str(self.subtipo.GetValue())
        self.cbS = str(self.cb.GetValue())
        self.cbNN = str(self.cbN.GetValue())
        self.nicoti = str(self.nico.GetValue())
        self.liqstock = str(self.stock.GetValue())
        self.subtipoN = str(self.subtipoB.GetValue())
        
        if self.cbS == "Otro":
            self.cbS = self.cbNN
        if self.cbS == "Frutal":
            self.subtipoT = "No tiene"
        if self.liqstock == "más":
            self.liqstock = str(self.masstock.GetValue())
        if self.subtipoT == "Otro":
            self.subtipoT = self.subtipoN
        for i in range (len(self.liquidosT)):
            self.lista = str(self.liquidosT[i].GetValue())

        self.list.append(self.lista)
        self.list.append(self.liqstock)
        self.list.append(self.cbS)
        self.list.append(self.subtipoT)
        self.list.append(self.nicoti)

        for i in range(len(self.list)):
            if i == 0:
                nom = self.list[i]
                self.listaT.append(self.list[i])
            if i == 1:
                liq = self.list[i]
                self.listaT.append(self.list[i])
            if i == 2:
                cb = self.list[i]
                self.listaT.append(self.list[i])
            if i == 3:
                subTip = self.list[i]
                self.listaT.append(self.list[i])
            if i == 4:
                nicotina =  self.list[i]
                self.listaT.append(self.list[i])

        self.cargarClienteSql(self.list)
        self.dvlc.AppendItem([nom, liq, cb, subTip, nicotina])
        self.v2.Close()
    
    def cargarClienteSql(self, lista):
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        try:
            cur.execute('''CREATE TABLE IF NOT EXISTS Liquidos(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            Líquidos NVARCHAR NOT NULL,
            Stock NVARCHAR NOT NULL,
            Tipo NVARCHAR NOT NULL,
            Subtipo NVARCHAR NOT NULL,
            Nicotina NVARCHAR NOT NULL)''')
        except:
            pass
        cur.executemany("INSERT INTO liquidos VALUES (NULL,?,?,?,?,?)", (lista, ))
        con.commit()
        con.close()
    
    def mostrarClientes(self):
        self.dvlc.DeleteAllItems()
        lista = self.recuperoDBclientes()
        for i in range(len(lista)):
            self.dvlc.AppendItem(lista[i])

    def recuperoDBclientes(self):
        lista = []
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM liquidos ORDER BY id")
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        print(listaA)
        for i in range(len(listaA)):
            lista.append(listaA[i][1:])
        for e in lista:
            e[0] = str(e[0])    
        con.close()
        return lista

    def editar (self, event):
        self.row = row = self.dvlc.GetSelectedRow()
        nomEditar = self.dvlc.GetTextValue(row, 0)
        liqEditar = self.dvlc.GetTextValue(row, 1)
        tipEditar = self.dvlc.GetTextValue(row, 2)
        subtipEditar = self.dvlc.GetTextValue(row, 3)
        nicoEditar = self.dvlc.GetTextValue(row, 4)


        self.v3 = v3 = Frame(None, title = "Ingresar el líquido")
        self.gbs1 = gbs = GridBagSizer(10,10)
        t1 = StaticText(v3, label = "Nombre")
        gbs.Add(t1, pos = (1,1))
        self.nom1 = nom = TextCtrl(v3, value = nomEditar)
        gbs.Add (nom, pos = (1,2))
        t2 = StaticText(v3, label = "Cantidad")
        gbs.Add(t2, pos = (2,1))
        elegir = []
        for i in range (11):
            n = str(i)
            elegir.append(n)
        elegir.append("más")
        self.stock1 = ComboBox(v3, value = liqEditar, choices = elegir, size = (100,35))
        gbs.Add(self.stock1, pos = (2,2))
        self.masstock1 = TextCtrl(v3, value = "Ingresar cantidad", size = (130,35))
        gbs.Add(self.masstock1, pos = (2,3))
        t3 = StaticText(v3, label = "Tipo")
        cblist = ["Tabaqui", "Frutal", "Otro"]
        self.cb1 = ComboBox(v3, value = tipEditar, choices = cblist, size = (100,35))
        gbs.Add(self.cb1, pos = (3,2))
        gbs.Add(t3, pos = (3,1))
        t4 = StaticText(v3, label = "Subtipo")
        gbs.Add(t4, pos = (4,1))
        self.subtipo1 = ComboBox (v3, value = subtipEditar, choices = ["Rubio", "Negro", "Otro"], size = (100,35))
        gbs.Add(self.subtipo1, pos = (4,2))
        self.subtipoB1 = TextCtrl(v3, value = "Ingresar", size = (100,35))
        gbs.Add(self.subtipoB1, pos = (4,3))
        t5 = StaticText(v3, label = "Nicotina")
        gbs.Add(t5, pos = (5,1))
        self.nico1 = ComboBox(v3, value = nicoEditar, choices = ["3","6"], size = (100,35))
        gbs.Add(self.nico1, pos = (5,2))
        self.agr1 = agr1 = Button(v3, label = "&Guardar")
        gbs.Add(agr1, pos = (6,1))
        self.liquidosT1 = []
        self.liquidosS1 = []
        self.liquidosT1.append(self.nom1)
        self.liquidosS1.append(self.stock1)
        self.agr1.Bind(EVT_BUTTON, self.guardar)
        self.cbN1 = TextCtrl(v3, value = "Ingrese el tipo", size = (110,35))
        self.gbs1.Add(self.cbN1, pos = (3,3))

        

        v3.SetSizerAndFit(gbs)
        v3.Show()    

    def guardar (self, event):
        self.list1 = []
        self.subtipoT1 = str(self.subtipo1.GetValue())
        self.cbS1 = str(self.cb1.GetValue())
        self.cbNN1 = str(self.cbN1.GetValue())
        self.nicoti1 = str(self.nico1.GetValue())
        self.liqstock1 = str(self.stock1.GetValue())
        self.subtipoN1 = str(self.subtipoB1.GetValue())
        
        if self.cbS1 == "Otro":
            self.cbS1 = self.cbNN1
        if self.cbS1 == "Frutal":
            self.subtipoT1 = "No tiene"
        if self.liqstock1 == "más":
            self.liqstock1 = str(self.masstock.GetValue())
        if self.subtipoT1 == "Otro":
            self.subtipoT1 = self.subtipoN1
        for i in range (len(self.liquidosT1)):
            self.lista1 = str(self.liquidosT1[i].GetValue())

        self.list1.append(self.lista1)
        self.list1.append(self.liqstock1)
        self.list1.append(self.cbS1)
        self.list1.append(self.subtipoT1)
        self.list1.append(self.nicoti1)

        for i in range(len(self.list1)):
            if i == 0:
                nom = self.list1[i]
            if i == 1:
                liq = self.list1[i]
            if i == 2:
                cb = self.list1[i]
            if i == 3:
                subTip = self.list1[i]
            if i == 4:
                nicotina =  self.list1[i]

        self.grabaBD(nom, liq, cb, subTip, nicotina, self.row)
        self.v2.Close()


    def grabaBD(self, nom, liq, cb, subTip, nicotina, id):   #Acá es donde quiero que guarde los datos en la base de datos
        engine = create_engine('sqlite:///puntodeventa.db')
        conn = engine.connect()
        metadata = MetaData()
        
        
        
        
        
                actu = "UPDATE datos SET * = '" + nom + liq + cb + subTip + nicotina + "' WHERE id = " + str(id)
        print(actu)
        cur.execute(actu)
        con.commit()
        con.close()

    def borrar (self, event):
        self.dvlc.DeleteItem(self.dvlc.GetSelectedRow())
app = MyApp()
app.MainLoop()
