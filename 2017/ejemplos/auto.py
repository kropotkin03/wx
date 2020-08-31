# -*- coding:utf8 -*-
from wx import *

class MiAppp(App):
    def OnInit(self):
        ventAgreg=Frame(None, -1, "Caracteristicas del nuvo auto", size=(500,300))

        p = self.p = Panel(ventAgreg,-1,size=(500,300))
        grilla = self.grilla=GridBagSizer(6,2)
        marcaList = ["Chevrolet", "Ford", "Fiat","Renault", "Volkswagen"]
        marc = self.marc = ComboBox(p, -1, "Marca", (90, 50), (160, -1), marcaList, CB_DROPDOWN | TE_PROCESS_ENTER )
        marc.Bind(EVT_KILL_FOCUS, self.OnKillFocus)
        self.modeloList = [["Clasic", "Agile", "Onix"],["Ka", "Fiesta"],["Siena", "Linea", "Palio", "Uno"],["Clio","Sandero","Logan", "Kangoo","Fluence"],["Up", "Trend", "Saveiro", "Fox","Suran", "Passat"] ]

        grilla.Add(marc, pos = (1,1), span = (1, 3))

        ventAgreg.Show()
        return True

    def OnKillFocus(self, evt):
        indice = self.marc.GetCurrentSelection()
        print indice
        evt.Skip()
        mod = self.mod = ComboBox(self.p, -1, "Modelo", (290, 50), (160, -1), self.modeloList[indice], CB_DROPDOWN | TE_PROCESS_ENTER )
        self.grilla.Add(mod, pos = (1,2), span = (1, 3))


prog = MiAppp()
prog.MainLoop()
