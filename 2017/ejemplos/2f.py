import wx
class DropTarget(wx.DropTarget):


     def __init__(self,textCtrl, *args, **kwargs):
          self.tc2 = kwargs.pop('tc2',None) #remove tc2 as it is not a valid keyword for wx.DropTarget
          super(DropTarget, self).__init__( *args, **kwargs)

          print self.tc2


class Frame(wx.Frame):

     def __init__(self, parent, tc2):
         #initialize the frame
         super(Frame,self).__init__(None,-1,"some title")
         self.tc2 = wx.TextCtrl(self, -1, size=(100, -1),pos = (170,60))#part number

def main():

     ex = wx.App(redirect=False)
     frame = Frame(None, None)
     frame.Show()
     #this is how you pass a keyword argument
     b = DropTarget(frame,tc2="something")
     ex.MainLoop()

if __name__ == '__main__':
    main()