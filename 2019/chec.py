from wx import *
from wx.dataview import *



class MyApp(App):
    def OnInit(self):
        f = Frame(None)
        p = Panel(f)
        dvlc = DataViewListCtrl(p)
        dvlc.AppendTextColumn("Marca", width=40)
        s = BoxSizer()
        c = CheckBox(p)
        c.Bind(EVT_CHECKBOX, self.foo)
        s.Add(dvlc)


        p.SetSizer(s)
        f.Show()
        return True


    def foo(self, event):
        print("check!")


app = MyApp()
app.MainLoop()
