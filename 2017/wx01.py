from wx import *

class MiAplicacion(App):

	def OnInit(self):
		self.res = xrc.XmlResource('ej01.xrc')
		self.frame = self.res.LoadFrame(None, 'MyFrame3')
		self.frame.Show()

		return True


LaAplicacion = MiAplicacion()

LaAplicacion.MainLoop()