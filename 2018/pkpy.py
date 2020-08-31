from wx import *

f = []
newf = -1
class PKframe(Frame):
    def __init__(self, name=FrameNameStr, parent = None, id = ID_ANY, title = "", pos = DefaultPosition, size = DefaultSize, style = DEFAULT_FRAME_STYLE):
        Frame.__init__(self, parent, id, title, pos, size, style, name)


class PKpanel(Panel):
    def __init__(self, fName, fSize = DefaultSize, id=ID_ANY, pos=DefaultPosition, size=DefaultSize, style=TAB_TRAVERSAL, name=PanelNameStr):
        noExiste = True
        for v in f:
            if v.GetName() == fName:
                noExiste = False
        if noExiste:
            fr = PKframe(fName, fSize)
            f.append(fr)
            indi = -1
            Panel.__init__(self, f[indi], id, pos, size, style, name)
        else:
            mensaje = "Ya existe el frame " + fName
            MessageBox(mensaje)





