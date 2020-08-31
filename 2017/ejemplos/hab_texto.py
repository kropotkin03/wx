from wx import *

class MiApp(App):
	def OnInit(self):
		f = Frame(None, -1)
		p1 = self.p1 = Panel(f, -1, size = (300, 200))
		p1.SetBackgroundColour("#ff0000")
		p2 = self.p2 = Panel(f, -1, size = (300, 200))
		p2.SetBackgroundColour("#0000ff")
		b = BoxSizer(VERTICAL)
		c = self.c = CheckBox(p1, -1, "hola")
		print self.c.GetValue()
		texto = self.texto = TextCtrl(self.p2, -1, "", border = 10, style)
		texto.Disable()
		b.Add(p1, 0)
		b.Add(p2, 0)
		c.Bind(EVT_LEFT_DOWN  , self.onClick)
		f.SetSizer(b)
		f.Show()
		return True

	def onClick(self, evt):
		evt.Skip()
		print self.c.GetValue()
		if self.c.GetValue() == False:
			self.texto.Enable()
		else:
			self.texto.Disable()


app = MiApp()
app.MainLoop()