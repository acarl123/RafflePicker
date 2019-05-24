from mainview import MainFrame
import wx
import csv
import os
import random

class Controller:
    def __init__(self, parent=None):
        self.mainWindow = MainFrame(parent)

        # setup View
        self.mainWindow.fpCSVInput.wildcard="CSV Files (*.csv)|*.csv"
        
        # setup Bindings
        self.mainWindow.Bind(wx.EVT_BUTTON, self.onPickWinner, self.mainWindow.btnCalculate)
    
    def show(self):
        self.mainWindow.Show()
    
    def onPickWinner(self, event):
        entryFile = self.mainWindow.fpCSVInput.GetPath()
        _, ext = os.path.splitext(entryFile)
        if not ext.lower() == ".csv":
            MyMessageDialog(self.mainWindow, "please only select a .csv file")
            return

        weighted_random = []
        with open(entryFile, "rb") as csvfile:
            csvReader = csv.reader(csvfile)
            for row in csvReader:
                try:
                    row = [entry.decode("utf8") for entry in row]
                    weighted_random += [row[0]] * int(row[1])
                except Exception as e:
                    MyMessageDialog(self.mainWindow, e.message)
                    return
        
        winner = random.choice(weighted_random)
        MyMessageDialog(self.mainWindow, "The winner is: %s!" % winner, caption="Winrar!")

class MyMessageDialog:
    def __init__(self, parent, message, caption='', buttons=wx.OK):
        self.parent = parent
        self.message = message
        self.caption = caption
        self.buttons = buttons
        self.show()
    
    def show(self):
        msgDlg = wx.MessageDialog(self.parent, self.message, caption=self.caption, style=self.buttons)
        msgDlg.ShowModal()