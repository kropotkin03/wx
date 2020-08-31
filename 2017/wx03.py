import wx
from wx import xrc

class MiAplicacion(wx.App):

	def OnInit(self):
		self.res = xrc.XmlResource('ej03.xrc')
		self.init_frame()

		return True

	def init_frame(self):
		self.frame = self.res.LoadFrame(None, 'MyFrame4')

		self.botonAceptar = xrc.XRCCTRL(self.frame, 'm_button9')
		self.frame.Bind(wx.EVT_BUTTON, self.mostrar_bienvenida, self.botonAceptar)

		self.botonCancelar = xrc.XRCCTRL(self.frame, 'm_button10')
		self.frame.Bind(wx.EVT_BUTTON, self.salir, self.botonCancelar)

		self.frame.Show()

	def mostrar_bienvenida(self, event):
		wx.MessageBox('Bienvenido!')

	def salir(self, event):
		self.frame.Close()


app = MiAplicacion()

app.MainLoop()
