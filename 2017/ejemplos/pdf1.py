import wx

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from reportlab.lib.pagesizes import landscape

class MyFrame1 ( wx.Frame ):

    def __init__( self ):
        wx.Frame.__init__ ( self, None,
                            size = wx.Size( 250,150 ),
                            style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        DataBox = wx.BoxSizer( wx.HORIZONTAL )

        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        self.NameLabel = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.NameLabel.Wrap( -1 )
        self.NameLabel.SetFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )

        gSizer2.Add( self.NameLabel, 0, wx.ALL, 5 )

        self.NameField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.NameField, 1, wx.ALL, 5 )

        self.SaveToPDF = wx.Button( self, wx.ID_ANY, u"Save To PDF", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.SaveToPDF, 0, wx.ALL, 5 )


        DataBox.Add( gSizer2, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.SetSizer( DataBox )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.SaveToPDF.Bind( wx.EVT_BUTTON, self.SaveToPDF_Function )

        self.Show()

    #----------------------------------------------------------------------
    def create_pdf(self):
        """"""
        nameString = str(self.NameField.GetValue())
        nameString += ".pdf"
        c = canvas.Canvas(nameString, pagesize=landscape(A3))

        txt = """'I want this to open only after I clicked the "Save To PDF"
        button. Also, the text field value (NameString variable) should appear
        here =>'  + %s """ % nameString
        c.drawCentredString(600, 800, txt)

        c.save()


    # Virtual event handlers, overide them in your derived class
    def SaveToPDF_Function( self, event ):
        self.create_pdf()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1()
    app.MainLoop()