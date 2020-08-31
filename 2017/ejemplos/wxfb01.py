# -*- coding: utf-8 -*-

import wx
import wx.xrc

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		m_radioBox1Choices = [ u"uno", u"dos", u"tres" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer1.Add( self.m_radioBox1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, "", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.m_radioBox1.Bind( wx.EVT_KILL_FOCUS, self.kFocusRB )

	def __del__( self ):
		pass

	def kFocusRB( self, event ):
		im = self.m_radioBox1.GetString(self.m_radioBox1.GetSelection())
		self.m_staticText1.SetLabel(im)
		event.Skip()


app = wx.App()
f = wx.Frame(None)
p = MyPanel1(f)
f.Show()
app.MainLoop()