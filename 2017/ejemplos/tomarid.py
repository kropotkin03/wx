from wx import *
from ej04 import *

class Saludos(Ventana):
	def __init__(self):
		Ventana.__init__(self, None)
		self.b_bienvenido.Bind(EVT_BUTTON, self.mostrar_bienvenida)
		self.b_cartelito.Bind(EVT_BUTTON, self.mostrar_cartelito)

	def mostrar_bienvenida(self, event):
		MessageBox('Bienvenido!')

	def mostrar_cartelito(self, event):
		self.t_cartelito.SetLabel("cartelitooooooooooo")


class MiAplicacion(App):

	def OnInit(self):
		self.frame = Saludos()
		self.frame.Show()
		return True


app = MiAplicacion()
app.MainLoop()
