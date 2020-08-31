from wx import *
from ej03 import *

class Cual(MyFrame4):
	def __init__(self, parent):
		MyFrame4.__init__(self, None)
		self.m_button9.Bind(EVT_BUTTON, self.mostrar_bienvenida)
		self.m_button10.Bind(EVT_BUTTON, self.salir)

	def mostrar_bienvenida(self, event):
		MessageBox('Bienvenido!')

	def salir(self, event):
		self.parent.Close()


class MiAplicacion(App):

	def OnInit(self):
		self.frame = Cual(None)


		self.frame.Show()
		return True



app = MiAplicacion()

app.MainLoop()
