# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Ventana
###########################################################################

class Ventana ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ventana de Ejemplo", pos = wx.DefaultPosition, size = wx.Size( 340,164 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.b_bienvenido = wx.Button( self, wx.ID_ANY, u"Bienvenido", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizer3.Add( self.b_bienvenido, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.b_cartelito = wx.Button( self, wx.ID_ANY, u"Cartelito", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.b_cartelito, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.t_cartelito = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.t_cartelito.Wrap( -1 )
		bSizer3.Add( self.t_cartelito, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

