from wx import *

class MiApp(App):
	def OnInit(self):
		f = Frame(None, -1, '', size = (400, 400), style = CAPTION | CLOSE_BOX)
		p = Panel(f, -1, style = wx.TAB_TRAVERSAL)
		p.SetBackgroundColour("#009999")
		bs = GridBagSizer(20, 20)
		t1 = StaticText(p, -1, "Ingrese nombre")
		t2 = StaticText(p, -1, "Nombres")
		ct = self.ct = TextCtrl(p, -1, "Nombre")
		bo = Button(p, -1, "Agregar")
		bl = self.bl = ListBox(p, -1)
		bs.Add(t1, (0, 0))
		bs.Add(t2, (0, 1))
		bs.Add(ct, (1, 0))
		bs.Add(bo, (2, 0))
		bs.Add(bl, (1, 1), span = (2, 1))
		p.SetSizer(bs)
		f.Show()
		bo.Bind(EVT_BUTTON, self.onClickBoton)
		ct.Bind(EVT_LEFT_DOWN, self.onClickNombre)
		return True

	def onClickBoton(self, e):
		self.bl.Append(self.ct.GetValue())

	def onClickNombre(self, e):
		self.ct.SetValue("")
		e.Skip()

app = MiApp()
app.MainLoop()
