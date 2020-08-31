from wx import *
from ej03 import *


class MiAplicacion(App):

	def OnInit(self):
		self.frame = MyFrame4()
		self.frame.Show()
		return True

	def mostrar_bienvenida(self, event):
		MessageBox('Bienvenido!')


LaAplicacion = MiAplicacion()
LaAplicacion.MainLoop()