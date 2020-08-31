from wx import *
import os

wildcard = "Python source (*.py)|*.py|"     \
           "Compiled Python (*.pyc)|*.pyc|" \
           "SPAM files (*.spam)|*.spam|"    \
           "Egg file (*.egg)|*.egg|"        \
           "All files (*.*)|*.*"

class A(App):
    def OnInit(self):
        f = Frame(None)
        s = BoxSizer()
        a = Button(f, -1, "Abrir")
        b = Button(f, -1, "Guardarrrrrrrr")
        s.Add(a)
        s.Add(b)
        a.Bind(EVT_BUTTON, self.abrir)
        b.Bind(EVT_BUTTON, self.guardar)
        f.SetSizer(s)
        f.Show()

        return True


    def abrir(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            None,
            message="Choose a file",
            defaultDir="",
            defaultFile="",
            wildcard=wildcard,
            #style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            style=FD_DEFAULT_STYLE
        )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print "You chose the following file(s):"
            for path in paths:
                print path
        dlg.Destroy()

    def guardar(self, event):
        """
        Create and show the Save FileDialog
        """
        dlg = wx.FileDialog(
            None, message="Save file as ...",
            defaultDir="",
            defaultFile="",
            wildcard=wildcard,
            style=FD_SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print "You chose the following filename: %s" % path
        dlg.Destroy()

a = A()
a.MainLoop()
