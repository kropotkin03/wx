import wx
import wx.lib.scrolledpanel

class SimpleFrame(wx.Frame):
    def __init__(self, parent):
        super(SimpleFrame, self).__init__(parent)

        # add a panel so it looks the correct on all platforms
        self.frame_panel = wx.Panel(self)
        frame_panel = self.frame_panel
        # image panel
        self.image_panel = wx.lib.scrolledpanel.ScrolledPanel(frame_panel, style=wx.SIMPLE_BORDER)
        image_panel = self.image_panel
        image_panel.SetAutoLayout(True)
        image_panel.SetupScrolling()
        # image panel - image control
        self.image_ctrl = wx.StaticBitmap(image_panel)
        self.image_ctrl.Bind(wx.EVT_MOTION, self.ImageCtrl_OnMouseMove)
        img = wx.Image("image.png", wx.BITMAP_TYPE_ANY)
        self.image_ctrl.SetBitmap(wx.BitmapFromImage(img))
        image_panel.Layout()
        image_sizer = wx.BoxSizer(wx.VERTICAL)
        image_sizer.Add(self.image_ctrl)
        image_panel.SetSizer(image_sizer)
        # frame sizer
        frame_sizer = wx.BoxSizer(wx.HORIZONTAL)
        frame_sizer.Add(image_panel, proportion=1, flag=wx.EXPAND | wx.ALL)
        frame_panel.SetSizer(frame_sizer)
        return

    def ImageCtrl_OnMouseMove(self, event):
        # position in control
        ctrl_pos = event.GetPosition()
        print("ctrl_pos: " + str(ctrl_pos.x) + ", " + str(ctrl_pos.y))
        # position in image
        #image_pos = ??? convert control position to image position
        #print("image_pos: " + str(image_pos.x) + ", " + str(image_pos.y))


app = wx.PySimpleApp()
frame = SimpleFrame(None)
frame.Show()
app.MainLoop()