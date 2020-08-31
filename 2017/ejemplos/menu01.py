from wx import *

class MyApp(App):
	def OnInit(self):
		f = Frame(None, -1, "")
		menuBar = MenuBar()
		f.CreateStatusBar()
		f.SetStatusText("")
		menu1 = Menu()
		menu1.Append(101, "&Mercury", "Mercurio es el primer planeta")
		f.Bind(EVT_MENU, self.Menu101, id=101)
		menu1.Append(102, "&Venus", "")
		menuBar.Append(menu1, "&Planets")
		f.SetMenuBar(menuBar)
		f.Show()
		return True

	def Menu101(self, event):
		MessageBox("Bienvenido a Mercurio", "Planetas", OK)


app = MyApp()
app.MainLoop()