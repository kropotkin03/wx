from wx import *
from ej03 import *


class MiAplicacion(App):

	def OnInit(self):
		self.frame = MyFrame4(None)

		self.botonAceptar = xrc.XRCCTRL(self.frame, 'm_button9')
		self.frame.Bind(EVT_BUTTON, self.mostrar_bienvenida, self.botonAceptar)

		self.botonCancelar = xrc.XRCCTRL(self.frame, 'm_button10')
		self.frame.Bind(EVT_BUTTON, self.salir, self.botonCancelar)

		self.frame.Show()
		return True

	def mostrar_bienvenida(self, event):
		MessageBox('Bienvenido!')

	def salir(self, event):
		self.frame.Close()


app = MiAplicacion()

app.MainLoop()
