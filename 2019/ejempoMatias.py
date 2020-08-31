from wx import *


class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        s = BoxSizer(VERTICAL)
        self.t1= t1 = TextCtrl(f)
        t1.Bind(EVT_KILL_FOCUS, self.algo)
        t2 = TextCtrl(f)
        s.Add(t1) 
        s.Add(t2)       
             
        
        f.SetSizer(s)
        f.Show()
        return True

    def algo(self, e):
        self.t1.SetValue("jaaaaaaaaaaaaa")



prog = MyApp()
prog.MainLoop()
