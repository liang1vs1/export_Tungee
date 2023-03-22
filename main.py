from tkinter import Frame
import wx
from TunGee import TG


def main():
    app = wx.App()
    frame = TG(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()