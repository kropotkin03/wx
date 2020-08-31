from wx import *

class MyApp(App):
    def OnInit(self):
        self.listaN = listaN = []
        self.listaS = listaS = []
        f1 = Frame(None, -1, title="Cargar Personas")
        gridBag = GridBagSizer(20, 20)
        boton = Button(f1, -1, label="Carga las minas wachin", )
        nombre = StaticText(f1, label="Nombres")
        
        for i in range (3):
            tN = TextCtrl(f1)
            gridBag.Add(tN, pos=(i+1,0))
            listaN.append(tN)
            self.sexos = sexos = ["Femenino", "Masculino"]
            self.botSexo = botSexo = RadioBox(f1, choices=sexos)
            listaS.append(botSexo)
            gridBag.Add(botSexo, pos=(i+1, 1))

        gridBag.Add(nombre, pos=(0,0))
        gridBag.Add(boton, pos=(4,1))
        boton.Bind(EVT_BUTTON, self.MuestroMinitas)
        f1.SetSizer(gridBag)
        f1.Show()    

        return True

    def MuestroMinitas(self, event):
        f2 = Frame(None, -1, title="Aca estan las minitas amiguito")
        gridBag2 = GridBagSizer(10, 0)
        minitas = StaticText(f2, label="Estas son las minitas")
        gridBag2.Add(minitas, pos=(0,0))
        j = 0
        for i in range(3):
            sexo = self.listaS[i].GetString(self.listaS[i].GetSelection())
            if sexo == "Femenino" :
                fem = self.listaN[i].GetValue()
                textMinitas = StaticText(f2)
                textMinitas.SetLabel(fem)
                gridBag2.Add(textMinitas, pos=(j+1, 0))
                j += 1 

        f2.SetSizer(gridBag2)
        f2.Show()
app = MyApp()
app.MainLoop()