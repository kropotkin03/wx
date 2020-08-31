from wx import *
from random import *

class MyApp(App):
    def OnInit(self):
    #Linux
        f = Frame(None, size=(800,600), pos=(280,100),style= RESIZE_BORDER) 
        bg = StaticBitmap(f, ID_ANY, Bitmap('WxPython/casinobg2.jpg'), pos=(0, 0))      
        titu = StaticText(f, label="Bienvenido a la Suite de Juegos", pos=(175,150), size=(200,4)) 
        btn = Button(f, label="Juego del Punto", pos=(330,350))
        #btn2 = Button(f, label="Juego del Craps", pos=(331,350))
        btn3 = Button(f, label="Salir", pos=(347,400))
    #Windows
        '''f = Frame(None, size=(800,600), pos=(550,160),style= RESIZE_BORDER) 
        bg = StaticBitmap(f, ID_ANY, Bitmap('test/casinobg2.jpg'), pos=(0, 0))
        titu = StaticText(bg, label="Bienvenido a la Suite de Juegos", pos=(185,180))
        btn = Button(bg, label="Juego del Punto", pos=(330,350))
        #btn2 = Button(bg, label="Juego del Craps", pos=(331,350))
        btn3 = Button(bg, label="Salir", pos=(337,400))'''

    #
        sizer = BoxSizer(VERTICAL)     
        titu.SetBackgroundColour((219,212,247))
        #titu.SetForegroundColour((119,232,77))
        titu.SetFont(Font(18, MODERN, NORMAL, BOLD, False, u'Consolas'))
     
        sizer.Add(titu, 0, ALL, 5)
        sizer.Add(btn, 0, ALL, 5)
        #sizer.Add(btn2, 0, ALL, 5)
        sizer.Add(btn3, 0, ALL, 5)
        btn.Bind(EVT_BUTTON, self.JPunto)
        btn3.Bind(EVT_BUTTON, self.OnQuit)

        f.Show()
        
        return True

    def JPunto(self, e):  
    # Linux
        die = Image('WxPython/default.png').ConvertToBitmap()
        self.f = f = Frame(None, title="Juego del Punto", size=(600,450),pos=(380,150),style= CAPTION | CLOSE_BOX | RESIZE_BORDER)
        bg = StaticBitmap(f, ID_ANY, Bitmap('WxPython/punto.jpg'), pos=(0, -100))

        self.dado1 = StaticBitmap(f, ID_ANY, die, pos=(150, 150))
        self.dado2 = StaticBitmap(f, ID_ANY, die, pos=(280, 150))
        self.dado3 = StaticBitmap(f, ID_ANY, die, pos=(215, 225))

        self.btn = btn = Button(f, label="Tirar Dados", pos=(480,80))
        btn.Hide()
        self.btn2 = btn2 = Button(f, label="Apostar", pos=(482,80))
        btn3 = Button(f, label="Instrucciones", pos=(480,120))
        #btn4 = Button(f, label="Salir", pos=(480,190))
        titup = StaticText(f, label="Puntaje Jugador", pos= (28,300), size=(120,0))
        titup2 = StaticText(f, label="Puntaje PC", pos= (30,350), size=(120,0))
        puntaje = self.puntaje = StaticText(f, label="0", pos= (30,320), size=(60,20))
        puntaje2 = self.puntaje2 = StaticText(f, label="0", pos= (30,370), size=(60,20))
        bonus = self.bonus = StaticText(f, label=(""), pos=(120,320))
        bonus.SetForegroundColour((50,200,20))
        bonus2 = self.bonus2 = StaticText(f, label=(""), pos=(120,370))
        bonus2.SetForegroundColour((50,200,20))
    #Windows
        '''die = Image('test/default.png').ConvertToBitmap()
        self.f = f = Frame(None, title="Juego del Punto", size=(600,450),pos=(650,250),style= CAPTION | CLOSE_BOX | RESIZE_BORDER)
        bg = StaticBitmap(f, ID_ANY, Bitmap('test/punto.jpg'), pos=(22, 55))
      
        self.dado1 = StaticBitmap(bg, ID_ANY, die, pos=(150, 150))
        self.dado2 = StaticBitmap(bg, ID_ANY, die, pos=(280, 150))
        self.dado3 = StaticBitmap(bg, ID_ANY, die, pos=(215, 225))

        self.btn = btn = Button(bg, label="Tirar Dados", pos=(480,80))
        btn.Hide()
        self.btn2 = btn2 = Button(bg, label="Apostar", pos=(480,80))
        btn3 = Button(bg, label="Instrucciones", pos=(480,120))
        #btn4 = Button(f, label="Salir", pos=(480,190))
        titup = StaticText(bg,label=("Puntaje"), pos=(30,360))
        puntaje = self.puntaje = StaticText(bg, label=("0"), pos=(30,380), size=(50,20))
        bonus = self.bonus = StaticText(bg, label=(""), pos=(90,380))'''
    #
        s = BoxSizer(VERTICAL)
        cant = self.cant = 0
        punt_j = self.punt_j = 0  
        punt_pc = self.punt_pc = 0
        doble = self.doble = False

        titup.SetFont(Font(10, SWISS, NORMAL, BOLD))
        titup.SetForegroundColour((10,10,10))      
        puntaje.SetBackgroundColour(WHITE)
        titup2.SetFont(Font(10, SWISS, NORMAL, BOLD))
        titup2.SetForegroundColour((10,10,10))      
        puntaje2.SetBackgroundColour(WHITE)

        s.Add(btn, 0, ALL, 5)
        s.Add(btn2, 0, ALL, 5)
        s.Add(btn3, 0, ALL, 5)
        s.Add(puntaje, 0, ALL, 5)
        s.Add(titup, 0, ALL, 5)
        btn.Bind(EVT_BUTTON, self.PuntoDado)
        btn2.Bind(EVT_BUTTON, self.PuntoApu)
        btn3.Bind(EVT_BUTTON, self.OnAbout)
        #btn4.Bind(EVT_BUTTON, self.OnClose) #Close frame
        f.Show()

        
    def tirada(self):
    #Linux
        die = ["relleno"]
        for i in range(1,7):
            img = 'WxPython/die' + str(i) + '.png'
            die.append(Image(img).ConvertToBitmap())
        a = randint(1,6)
        sum = [0, 1, 0, 2, 0, 4, 0]
        return a, die[a], sum[a] 

    def test(self):
        die6 = Image('WxPython/die6.png').ConvertToBitmap()
        a = 6
        b = 6
        c = 6

        return a,b,c,die6,die6,die6
        
    def PuntoDado(self,event):
        self.cant += 1
        if self.cant <=4:
            a,Img,punt_a = self.tirada()
            b,Img2,punt_b = self.tirada()
            c,Img3,punt_c= self.tirada()
            self.punt_j += punt_a+punt_b+punt_c

            #a,b,c,asd,asd2,asd3 = self.test()

            if a == b == c and a%2 == b%2 == c%2 == 0 :
                self.doble = True
                self.bonus.SetLabel("¡¡ BONUS X2 !!")

            if self.cant == 4:
                if  self.doble == True:
                    self.punt_j = self.punt_j*2
                self.player2()
            self.puntaje.SetLabel(str(self.punt_j))                
            self.dado1.SetBitmap(Img)        
            self.dado2.SetBitmap(Img2)
            self.dado3.SetBitmap(Img3)

        
    def PuntoApu(self,event):
    #Linux
        self.f2 = f2 = Frame(None, -1, "Apuesta", size = (450, 150), pos=(530,150), style = RESIZE_BORDER|CAPTION|CLOSE_BOX)
        p2 = self.p2 = Panel(f2, -1, style = TAB_TRAVERSAL)
        grilla = GridBagSizer(1,2)
        self.guardar = guardar = Button(p2, -1, "&Guardar")
        grilla.Add(guardar, pos = (3, 0))
    #Windows
        '''self.f2 = f2 = Frame(None, -1, "Apuesta", size = (250, 250), pos=(1000,250), style = RESIZE_BORDER|CAPTION|CLOSE_BOX)
        p2 = self.p2 = Panel(f2, -1, style = TAB_TRAVERSAL)
        grilla = GridBagSizer(1,2)
        guardar = guardar = Button(p2, -1, "&Guardar")
        grilla.Add(guardar, pos = (2, 1))'''
    #
        l_imp = StaticText(p2, -1, "Importe")
        grilla.Add(l_imp, pos = (1,0))
        impList = ["$100", "$200", "$300", "$500", "$1000"]
        self.imp = imp = RadioBox(p2, -1, "", DefaultPosition, DefaultSize, impList, 1, NO_BORDER)
        grilla.Add(imp, pos = (1, 2))
        
        guardar.Bind(EVT_BUTTON, self.OnClose)
        p2.SetSizerAndFit(grilla)
        f2.Show()
    

    def OnAbout(self, e):
        """ the about box """
        about = MessageDialog( None, "La idea general del Juego del Punto es lograr el máximo puntaje en 4 lanzamientos.\n"
        "Sólo suman puntaje los dados que salgan con un punto en el centro (el 1, el 3 y el 5). \n"
        "El puntaje de la tirada se calcula sumando el aporte de cada dado según la cantidad de puntos alrededor del centro.\n\n"
        "Si en alguna de las tiradas salen tres números pares iguales, se duplicaran los puntos finales.\n\n"
        "Se debe realizar una apuesta para empezar." 
        , "Instrucciones ", OK)
        about.ShowModal()
        about.Destroy()

    def OnClose(self, event):
        im = self.imp.GetString(self.imp.GetSelection())
        self.im = int(im[1:])
        print('apuesta: '+str(self.im)) #test
        self.comision()
        self.btn2.Hide() 
        self.btn.Show() 
        self.f2.Close()

    def player2(self):
        sum = 0
        doble = False

        for i in range(4):
            a,Img,punt_a = self.tirada()
            b,Img,punt_b = self.tirada()
            c,Img,punt_c = self.tirada()
            print(a,b,c)
            #a,b,c,Img,Img2,Img3 = self.test()
            if a == b == c and a%2 == b%2 == c%2 == 0 :
                doble = True
                self.bonus2.SetLabel("¡¡ BONUS X2 !!")

            self.punt_pc += punt_a+punt_b+punt_c
            print(self.punt_pc)

        if  doble == True:
            self.punt_pc = self.punt_pc*2
        self.puntaje2.SetLabel(str(self.punt_pc))  
        self.ganador()


    def comision(self):
        if self.im <= 500:
            porc = ((15*self.im*2)/100)  # apuesta*2 (apuesta_jugador_1 = apuesta_jugador_2)
            c = round(porc)
        else:
            porc = ((25*self.im*2)/100)
            c = round(porc)
        self.com = c
        print('comision (% de apuesta x2): '+str(self.com)) #test
        self.ganancia()

    def ganancia(self):
        g = (self.im*2 - self.com)
        self.gan = g
        print('ganancia (apuesta x2 - comision): '+str(self.gan)) #test

    def ganador(self):
        self.f3 = f3 = Frame(None, title="Fin de la Partida", size=(450,120),pos=(460,200),style= CAPTION | CLOSE_BOX )
        titu = StaticText(f3, label="", pos=(175,150), size=(300,4)) 
        
        if self.punt_j > self.punt_pc:
            may = 'Jugador'
            total = self.punt_j
            titu.SetLabel(" \nFelicitaciones "+may+"!. Ha ganado la partida con "+str(total)+" puntos.\n\n"
            " El premio es de $"+str(self.gan)+".\n El casino se queda con una comisión de $"+str(self.com)+".")
        elif self.punt_j < self.punt_pc:
            may = 'PC'
            total = self.punt_pc
            titu.SetLabel(" Game Over, "+may+" ha ganado la partida con "+str(total)+" puntos.\n\n"
            " La casa ganó $"+str(self.im*2)+".\n Gracias vuelva prontos.")
        else:
            titu.SetLabel("\n\nGame Over, la partida terminó en un empate.\n"
            "Las apuestas fueron devueltas.")
        
        f3.Show()

    def OnQuit(self, event):
        Exit()
        

app = MyApp()
app.MainLoop()