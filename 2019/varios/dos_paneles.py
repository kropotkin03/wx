from wx import *


class MyApp(App):
     def OnInit(self):
         frame = Frame(None, -1, size=(250, 250))
         panel1 = Panel(frame)
         panel1.SetBackgroundColour('#ff0000')
         button1 = Button(panel1)
         panel2 = Panel(frame)
         panel2.SetBackgroundColour('#00ff00')
         button2 = Button(panel2)
         sizer = BoxSizer(VERTICAL)
         sizer.Add(panel1,0,EXPAND|ALL,10)
         sizer.Add(panel2,0,EXPAND|ALL,10)
         frame.SetSizer(sizer)
         frame.Show(True)
         return True

app = MyApp(0)
app.MainLoop()