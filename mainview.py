# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version May 23 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Raffle Picker 9001", pos = wx.DefaultPosition, size = wx.Size( 337,110 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Entry File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.fpCSVInput = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.csv", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer1.Add( self.fpCSVInput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.btnCalculate = wx.Button( self, wx.ID_ANY, u"Pick a Winner!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btnCalculate, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


