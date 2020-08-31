from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "")
        b = Button(f, -1, "")
        b.Bind(EVT_BUTTON, self.sonido)
        f.Show()
        return True

    def sonido(self, e):
        sound = Sound("alarm.wav")
        sound.Play(SOUND_ASYNC)

app = MyApp()
app.MainLoop()
