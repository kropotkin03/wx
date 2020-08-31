from wx import *
from ej05 import *

class Saludos(Ventana):
	def __init__(self):
		Ventana.__init__(self, None)

		self.b_bienvenido.Bind(EVT_BUTTON, self.mostrar_bienvenida)
		self.b_cartelito.Bind(EVT_BUTTON, self.mostrar_cartelito)

	def mostrar_bienvenida(self, event):
		MessageBox('Bienvenido!')

	def mostrar_cartelito(self, event):
		f2 = MiVentana()

		f2.Show()

class MiVentana(Ventana2):
	def __init__(self):
		Ventana2.__init__(self, None)
		self.m_textCtrl1.SetValue("pablokan")


class MiAplicacion(App):

	def OnInit(self):
		self.frame = Saludos()
		self.frame.Show()
		return True


app = MiAplicacion()
app.MainLoop()
