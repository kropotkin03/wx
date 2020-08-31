from wx import *


class MyApp(App):
    def OnInit(self):
        f1 = Frame(None, -1, 'titulo')
        self.ventana = ventana = Panel(f1, size = (800, 600))
        ventana.SetBackgroundColour("blue")
        bSizer2 = BoxSizer(VERTICAL)

        m_button4 = Button(ventana, ID_ANY, "saludar", DefaultPosition, DefaultSize, 0)
        m_button4.Bind(EVT_BUTTON, self.hola)
        bSizer2.Add(m_button4, 0, EXPAND, 5)

        m_button5 = Button(ventana, ID_ANY, "a rojo!", DefaultPosition, DefaultSize, 0)
        bSizer2.Add(m_button5, 0, ALIGN_CENTER|ALL, 5)
        m_button5.Bind(EVT_BUTTON, self.rojo)

        m_button6 = Button(ventana, ID_ANY, u"MyButton", DefaultPosition, DefaultSize, 0)
        bSizer2.Add(m_button6, 0, SHAPED, 5)
        ventana.SetSizer(bSizer2)
        ventana.Layout()

        f1.Show()
        return True

    def hola(self, event):
        MessageBox("hola")

    def rojo(self, event):
        self.ventana.SetBackgroundColour("red")
        self.ventana.Refresh()
app = MyApp()
app.MainLoop()

