# -*- coding:utf-8 -*-

from wx import *
from wx.dataview import *
#import sqlite3

class MyApp(App):
    def OnInit(self):

        frPrinc = Frame(None,-1,"CalcuCalo", size = (700,550))
        p1 = self.p1 = Panel(frPrinc ,-1)
        #BOTONES
        bC = self.bC = Button(p1, -1, "&CALCULAR",size = (700,50))
        bA = self.bA = Button(p1, -1, "&AGREGAR",size = (700,50))
        bB = self.bB = Button(p1, -1, "&BORRAR",size = (700,50))
        bM = self.bM = Button(p1, -1, "&MODIFICAR",size = (700,50))
        bV = self.bV = Button(p1, -1, "&VER LISTA",size = (700,50))


        #BINDEO
        bC.Bind (EVT_BUTTON, self.cCalcular)
        bA.Bind (EVT_BUTTON, self.cAgregar)
        bB.Bind(EVT_BUTTON,self.cBorrar)
        bM.Bind(EVT_BUTTON,self.cModificar)
        bV.Bind (EVT_BUTTON, self.cVerLista)
        menuPrinc = BoxSizer (VERTICAL)

        menuPrinc.Add(self.bC, 5 , ALIGN_CENTER | ALL, 1)
        menuPrinc.Add(self.bA, 5 , ALIGN_CENTER | ALL, 1)
        menuPrinc.Add(self.bB, 5 , ALIGN_CENTER | ALL, 1)
        menuPrinc.Add(self.bM, 5 , ALIGN_CENTER | ALL, 1)
        menuPrinc.Add(self.bV, 5 , ALIGN_CENTER | ALL, 1)


        p1.SetSizer(menuPrinc)
        frPrinc.Show()

        return True

    def cAgregar(self,event):
        frAgre = self.frAgre = Frame (None, -1, "Agregar NUEVO alimento", size=(400,420))
        p2 = self.p2 = Panel(frAgre, -1)
        sizer2 = BoxSizer(VERTICAL)
        stN = self.stN = StaticText(p2, -1, "Nombre ")
        tcN = self.tcN = TextCtrl(p2, -1, "Nombre")
        stK = self.stK = StaticText(p2, -1, "Kcal ")
        tcK = self.tcK = TextCtrl(p2, -1, "Kcal")
        stH = self.stH = StaticText(p2, -1, "Hidratos ")
        tcH = self.tcH = TextCtrl(p2, -1, "Hidratos")
        stP = self.stP = StaticText(p2, -1, "Proteinas ")
        tcP = self.tcP = TextCtrl(p2, -1, "Proteínas")
        stL = self.stL = StaticText(p2, -1, "Lípidos ")
        tcL = self.tcL = TextCtrl(p2, -1, "Lípidos")
        sizer2.Add(self.stN, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.tcN, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.stK, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.tcK, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.stH, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.tcH, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.stP, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.tcP, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.stL, 0, ALIGN_LEFT | ALL, 3)
        sizer2.Add(self.tcL, 0, ALIGN_LEFT | ALL, 3)
        bAcep= self.bAcep = Button (p2,-1, "Aceptar")
        bAcep.Bind (EVT_BUTTON, self.cAceptarCarga)
        bCanc= self.bCanc = Button (p2,-1, "Cancelar")
        bCanc.Bind(EVT_BUTTON, self.cCancelarCarga)
        sizer2.Add(self.bAcep, 0 , ALIGN_CENTER | ALL, 4)
        sizer2.Add(self.bCanc, 0 , ALIGN_CENTER | ALL, 4)
        p2.SetSizer(sizer2)
        frAgre.Show()
        return True
    def cAceptarCarga(self,event):
        pass


    def cCancelarCarga(self,event):
        self.frAgre.Close()

    def cCalcular (self,event):
        dlgCant = TextEntryDialog(None, 'Cantidad de alimentos', "CALCULAR")
        sizer3= BoxSizer(HORIZONTAL)

        if dlgCant.ShowModal() == ID_OK:
            self.cAmt = cAmt = int(dlgCant.GetValue()) # add pk
            listaN = []
            listaK = []
            listaH = []
            listaP = []
            listaL = []

            frResu = Frame(None, -1, "RESULTADOS", size=(950, 550))
            pResu = self.pResu = Panel(frResu)
            self.dvlcResu = dvlcResu = DataViewListCtrl(pResu)

            encabezadoResu = [('ALIMENTO', 400),('GRAMOS',100),('KCALORIAS', 100), ('HIDRATOS-gr-', 100), ('PROTEÍNAS-gr-', 100),
                          ('LIPIDOS-gr-', 100)]
            for encaResu in encabezadoResu:
                dvlcResu.AppendTextColumn(encaResu[0], width=encaResu[1])

            sumK= 0
            sumL= 0
            sumH= 0
            sumP= 0
            for z in range (cAmt):
                todasLasListas = []
                dlgAlim = Dialog (None,-1,"Alimentos",size=(350,200))
                sisAlim = BoxSizer (VERTICAL)
                staCa = StaticText (dlgAlim,-1,"Alimentos de su comida.")
                textCa = TextCtrl (dlgAlim,-1,'Escriba aqui')
                okB = Button(dlgAlim, ID_OK,"&Aceptar")
                caB = Button(dlgAlim,ID_CANCEL, "&Cancelar")
                wx.CallAfter(textCa.SetFocus)
                sisAlim.Add(staCa, 0, ALIGN_CENTER | ALL, 5)
                sisAlim.Add(textCa, 0, ALIGN_CENTER | ALL, 5)
                sisAlim.Add(okB, 0, ALIGN_CENTER | ALL, 10)
                sisAlim.Add(caB, 0, ALIGN_CENTER | ALL, 10)
                dlgAlim.SetSizer(sisAlim)

                if dlgAlim.ShowModal() == ID_OK:

                    buscAli=self.buscAli = textCa.GetValue().upper()
                    largoAli= len(buscAli)
                    lista = []
                    listaAS= []
                    listaFilt= self.listaFilt= []
                    listaFiltI= self.listaFiltI= []
                    listaFiltN= self.listaFiltN= []
                    listaFiltK= self.listaFiltK= []
                    listaFiltH= self.listaFiltH= []
                    listaFiltP= self.listaFiltP= []
                    listaFiltL= self.listaFiltL= []

                    with open("tablaDeAlimentos.csv", "r+") as archivo:
                        for line in archivo:
                            line = line[:-1]
                            lista.append(line)

                        for t in lista:
                            t = t.split(",")
                            if t [1][:len(buscAli)].upper() == self.buscAli:
                                listaFilt.append(t)
                                listaFiltI.append(t[0])
                                listaFiltN.append(t[1])
                                listaFiltK.append(t[2])
                                listaFiltH.append(t[3])
                                listaFiltP.append(t[4])
                                listaFiltL.append(t[5])
                        #print self.listaFiltN

                        dlgAliX= self.dlgAlix= Dialog (None, -1, "Busque su alimento", size= (500,250))
                        #dlgAliX.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
                        sAlix = BoxSizer (VERTICAL)

                        dlgAliX.SetSizer(sAlix)
                        self.comboCa = comboCa = ComboBox(dlgAliX,500, "Alimentos", (500, 350), (500, -1), listaFiltN, CB_DROPDOWN | TE_PROCESS_ENTER)
                        #comboCa.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
                        okB = Button(dlgAliX, ID_OK)
                        caB = Button(dlgAliX, ID_CANCEL)

                        sAlix.Add(comboCa)
                        sAlix.Add(okB, 0, ALIGN_CENTER | ALL, 10)
                        sAlix.Add(caB, 0, ALIGN_CENTER | ALL, 10)

                        if dlgAliX.ShowModal() == ID_OK:
                            alimSele = self.alimSele = self.comboCa.GetValue()
                            #print self.alimSele
                            kSele = []
                            for z in range (len(listaFiltN)):
                                if listaFiltN[z] == alimSele:
                                    todasLasListas.append(alimSele)
                                    kSele = self.kSele = float(listaFiltK[z])
                                    hSele = self.hSele = float(listaFiltH[z])
                                    pSele = self.pSele = float(listaFiltP[z])
                                    lSele = self.lSele = float(listaFiltL[z])


                            dlgGr = Dialog(None,-1,"Gramos",size= (450,250))
                            sizGr = BoxSizer(VERTICAL)
                            staGr = StaticText (dlgGr,-1,alimSele)
                            textGr = self.textGr =  TextCtrl (dlgGr,-1,"cantidad de grs ")
                            bOkgr = Button(dlgGr,ID_OK, "&Aceptar")
                            bCANCELgr = Button(dlgGr,ID_CANCEL, "&Cancelar")
                            sizGr.Add(staGr, 0, ALIGN_CENTER | ALL, 10)
                            sizGr.Add(textGr, 0, ALIGN_CENTER | ALL, 10)
                            sizGr.Add(bOkgr, 0, ALIGN_CENTER | ALL, 10)
                            sizGr.Add(bCANCELgr, 0, ALIGN_CENTER | ALL, 10)

                            dlgGr.SetSizer(sizGr)
                            dlgGr.ShowModal()

                            getGr = int(textGr.GetValue())


                            todasLasListas.append(getGr)
                            totK = (getGr * float(kSele)) / 100
                            todasLasListas.append(totK)
                            totH = (getGr * float(hSele)) / 100
                            todasLasListas.append(totH)
                            totP = (getGr * float(pSele)) / 100
                            todasLasListas.append(totP)
                            totL = (getGr * float(lSele)) / 100
                            todasLasListas.append(totL)
                    self.dvlcResu.AppendItem(todasLasListas)
                    sumK+=float(todasLasListas[2])
                    sumH+=float(todasLasListas[3])
                    sumP+=float(todasLasListas[4])
                    sumL+=float(todasLasListas[5])

            itemTotal =[]
            itemTotal.append("TOTAL")
            itemTotal.append("")
            itemTotal.append(str(sumK))
            itemTotal.append(str(sumH))
            itemTotal.append(str(sumP))
            itemTotal.append(str(sumL))
            self.dvlcResu.AppendItem(itemTotal)
            self.dvlcResu.SelectRow(self.cAmt) # add pk

            horResu = BoxSizer(HORIZONTAL)
            sizer3Resu = BoxSizer(VERTICAL)
            sizer3Resu.Add(dvlcResu, 1, EXPAND)


            sizer3Resu.Add(horResu)
            pResu.SetSizer(sizer3Resu)
            frResu.Show()

        dlgCant.Destroy()







    def cAceptarCantidad(self,event):
        dlgAcepCant = self.dlgAcepCant = Dialog (None, "Calculadora")
        sizer4= BoxSizer(HORIZONTAL)
        bOK= Button (dlgAcepCant, ID_OK)
        bCA= Button (dlgAcepCant, ID_CANCEL)
        sizer4.Add(bOK, 0, ALIGN_CENTER | ALL, 10)
        sizer4.Add(bCA, 0, ALIGN_CENTER | ALL, 10)
        dlgAcepCant.SetSizer(sizer4)

    def cCancelarCantidad(self,event):
        self.frCant.Close()


    def cBorrar (self, event):
        dlgBorrar = Dialog (None,-1,"Borrar")
        sisBorrar = BoxSizer (VERTICAL)
        staBorrar = StaticText (dlgBorrar,-1,"Ingrese el alimento que desea borrar.")
        textBorrar = TextCtrl (dlgBorrar,-1,"ingrese aqui")
        bBacep = Button (dlgBorrar,ID_OK)
        bBcancel = Button (dlgBorrar,ID_CANCEL)
        sisBorrar.Add(staBorrar, 0, ALIGN_CENTER | ALL, 10)
        sisBorrar.Add(textBorrar, 0, ALIGN_CENTER | ALL, 10)
        sisBorrar.Add(bBacep, 0, ALIGN_CENTER | ALL, 10)
        sisBorrar.Add(bBcancel, 0, ALIGN_CENTER | ALL, 10)
        dlgBorrar.SetSizer(sisBorrar)
        dlgBorrar.ShowModal()

    def cModificar (self, event):
        dlgModificar = Dialog (None,-1,"Modificar")
        sisModificar= BoxSizer (VERTICAL)
        staModificar = StaticText (dlgModificar,-1,"Ingrese el alimento que desea Modificar.")
        textModificar = TextCtrl (dlgModificar,-1,"ingrese aqui")
        bMacep = Button (dlgModificar,ID_OK)
        bMcancel = Button (dlgModificar,ID_CANCEL)
        sisModificar.Add(staModificar, 0, ALIGN_CENTER | ALL, 10)
        sisModificar.Add(textModificar, 0, ALIGN_CENTER | ALL, 10)
        sisModificar.Add(bMacep, 0, ALIGN_CENTER | ALL, 10)
        sisModificar.Add(bMcancel, 0, ALIGN_CENTER | ALL, 10)
        dlgModificar.SetSizer(sisModificar)
        dlgModificar.ShowModal()

    def cVerLista (self,event):
        frList= Frame(None,-1,"LISTA DE ALIMENTOS CARGADOS- proporción valores: 100gr", size = (950,550))
        p3= self.p3 = Panel(frList,-1)
        self.dvlc= dvlc = DataViewListCtrl(p3)
        encabezado =[('ALIMENTO',400), ('KCALORIAS', 100), ('HIDRATOS-gr-', 100), ('PROTEÍNAS-gr-', 100), ('LIPIDOS-gr-',100)]
        for enca in encabezado:
            dvlc.AppendTextColumn (enca[0], width= enca[1])
        hor =BoxSizer(HORIZONTAL)
        sizer3= BoxSizer (VERTICAL)
        sizer3.Add(dvlc, 1, EXPAND)
        lista = []
        with open("tablaDeAlimentos.csv", "r+") as archivo:
            first = True
            for line in archivo:
                if first:
                    first = False
                else:
                    line = line[:-1]
                    lista.append(line)

        for e in lista:
            e = e.split(",")
            print e
            e.pop(0)
            print e

            self.dvlc.AppendItem(e)

        sizer3.Add(hor)
        p3.SetSizer(sizer3)
        frList.Show()

calcu = MyApp()
calcu.MainLoop()

