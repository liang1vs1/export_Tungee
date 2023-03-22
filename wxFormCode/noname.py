# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.UserName = wx.StaticText( self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UserName.Wrap( -1 )

		bSizer1.Add( self.UserName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.UserNameInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.UserNameInput, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.PassWord = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PassWord.Wrap( -1 )

		bSizer1.Add( self.PassWord, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.PassWordInput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer1.Add( self.PassWordInput, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Graber = wx.StaticText( self, wx.ID_ANY, u"负责人", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Graber.Wrap( -1 )

		bSizer1.Add( self.Graber, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		GraberListChoices = []
		self.GraberList = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, GraberListChoices, 0 )
		self.GraberList.SetSelection( 0 )
		bSizer1.Add( self.GraberList, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.subBtn = wx.Button( self, wx.ID_ANY, u"开始提取", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.subBtn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.done = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.done.Wrap( -1 )

		bSizer1.Add( self.done, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.UserNameInput.Bind( wx.EVT_TEXT_ENTER, self.UserNameText )
		self.PassWordInput.Bind( wx.EVT_TEXT_ENTER, self.PassWordText )
		self.GraberList.Bind( wx.EVT_CHOICE, self.GraberText )
		self.subBtn.Bind( wx.EVT_BUTTON, self.btn_submit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def UserNameText( self, event ):
		event.Skip()

	def PassWordText( self, event ):
		event.Skip()

	def GraberText( self, event ):
		event.Skip()

	def btn_submit( self, event ):
		event.Skip()


