from wx import *
from ej02 import *

class F2(MyFrame4):
	def __init__(self):
		MyFrame4.__init__(self, None)
		self.m_button9.Bind(EVT_BUTTON, self.mostrar_bienvenida)


	def mostrar_bienvenida(self, event):
		MessageBox('Bienvenido!')


class MiAplicacion(App):

	def OnInit(self):
		self.frame = F2()
		self.frame.Show()
		return True

LaAplicacion = MiAplicacion()
LaAplicacion.MainLoop()