from wx import *
from ej04 import *


class MiAplicacion(App, Ventana):

	def OnInit(self):
		#Ventana.__init__(self, None)
		self.frame = Ventana(None)


		self.b_bienvenido.Bind(EVT_BUTTON, self.mostrar_bienvenida)
		self.b_cartelito.Bind(EVT_BUTTON, self.mostrar_cartelito)
		self.frame.Show()
		return True

	def mostrar_bienvenida(self, event):
		MessageBox('Bienvenido!')

	def mostrar_cartelito(self, event):
		self.t_cartelito.SetLabel("cartelitooooooooooo")


app = MiAplicacion(None)
app.MainLoop()
