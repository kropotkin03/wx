from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, 'Combo Box Example', size=(350, 300))
        panel = Panel(f, -1)
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five','six', 'seven', 'eight']
        st = StaticText(panel, -1, "Select one:", (15, 15))
        cb1 = self.cb1 = ComboBox(panel, -1, "default value", (15, 30), DefaultSize,sampleList, CB_DROPDOWN)
        cb2 = ComboBox(panel, -1, "default value", (150, 30), DefaultSize,sampleList, CB_SIMPLE)
        cb1.Bind(EVT_COMMAND_ENTER, self.click)
        f.Show()
        print cb2.GetValue()
        return True

    def click(self, evt):
        print self.cb1.GetValue()

app = MyApp()
app.MainLoop()