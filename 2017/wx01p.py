from wx import *
from ej01 import *

class MiAplicacion(App):

	def OnInit(self):
		self.frame = MyFrame3(None)
		self.frame.Show()

		return True

LaAplicacion = MiAplicacion()

LaAplicacion.MainLoop()