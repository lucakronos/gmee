#! /usr/bin/python
# -*- coding: utf-8 _*_
# ventanaHija.py
# Get the GUI stuff
import wx

# We're going to be handling files and directories
import os

# Set up some button numbers for the menu
from wxPython.wx import *

ID_FILE_OPEN = wxNewId()
ID_FILE_CLOSE = wxNewId()
ID_FILE_EXIT = wxNewId()
ID_HELP_ABOUT = wxNewId()
ID_FILE_SAVE = wxNewId() 
 
class VentanaHija(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.NewId(), "Nombre del Sistema",
                          pos=(100,50),size=(930,580))
 
        self.panel = wx.Panel(self, -1)
        sizer1 = wx.BoxSizer(wx.VERTICAL)
        sizer1.Add(self.panel, 1, wx.EXPAND, 0)
 
        self.SetSizer(sizer1)
        self.Layout()
        self.Bind(wx.EVT_CLOSE, self.al_cerrar)

        #MenuBar
        file_menu = wxMenu()
        file_menu.Append(ID_FILE_OPEN, 'Open File')
        file_menu.AppendSeparator()
        file_menu.Append(ID_FILE_SAVE, "&Save"," Save file")
        file_menu.AppendSeparator()
        file_menu.Append(ID_FILE_CLOSE, 'Close File')
        file_menu.AppendSeparator()
        file_menu.Append(ID_FILE_EXIT, 'Exit Program')
        # create the 'Help' menu
        help_menu = wxMenu()
        help_menu.Append(ID_HELP_ABOUT, 'About')
        # we now need a menu bar to hold the 2 menus just created
        menu_bar = wxMenuBar()
        # add our menus to the menu bar. The first argument is the
        # menu (created above), and the second is what we want to
        # appear on the menu bar.
        #

        menu_bar.Append(file_menu, 'File')
        menu_bar.Append(help_menu, 'Help')
        # set the menu bar (tells the system we're done)
        self.SetMenuBar(menu_bar)
        # that's great! Now let's make the menu options do something!
        # Using EVT_MENU, we associate the identifier for each menu
        # item to a method to be called when the menu item is selected.
        # Most of these items will call the 'ToDo' function; essentially
        # a small stub method to tell the user something will happen,
        # but we have not got around to programming it, yet.
        #
        EVT_MENU(self, ID_FILE_OPEN, self.OnOpen)
        EVT_MENU(self, ID_FILE_CLOSE, self.ToDo)
        EVT_MENU(self, ID_FILE_EXIT, self.OnFileExit)
        EVT_MENU(self, ID_HELP_ABOUT, self.ToDo)
        EVT_MENU(self, ID_FILE_SAVE, self.OnSave); # just "pass" in our demo

        self.dirname = ''

    def OnFileExit(self, evt):
        """
        This is executed when the user clicks the 'Exit' option
        under the 'File' menu.  We ask the user if they *really*
        want to exit, then close everything down if they do.
        """
        dlg = wxMessageDialog(self, 'Exit Program?', 'I Need To Know!',
                              wxYES_NO | wxICON_QUESTION)
        if dlg.ShowModal() == wxID_YES:
            dlg.Destroy()
            self.Close(true)
        else:
            dlg.Destroy()


    def ToDo(self, evt):
        """
        A general purpose "we'll do it later" dialog box
        """
        dlg = wxMessageDialog(self, 'Not Yet Implimented!', 'ToDo',
                             wxOK | wxICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

 
    def al_cerrar(self, evt):
        #self.vntReferente.Show()
        self.vntReferente.Destroy()
        self.Destroy()

    def OnOpen(self,e):
        # In this case, the dialog is created within the method because
        # the directory name, etc, may be changed during the running of the
        # application. In theory, you could create one earlier, store it in
        # your frame object and change it when it was called to reflect
        # current parameters / values
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()

            # Open the file, read the contents and set them into
            # the text edit window
            filehandle=open(os.path.join(self.dirname, self.filename),'r')
            self.control.SetValue(filehandle.read())
            filehandle.close()

            # Report on name of latest file read
            self.SetTitle("Editing ... "+self.filename)
            # Later - could be enhanced to include a "changed" flag whenever
            # the text is actually changed, could also be altered on "save" ...
        dlg.Destroy()

    def OnSave(self,e):
        # Save away the edited text
        # Open the file, do an RU sure check for an overwrite!
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", \
                wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            itcontains = self.control.GetValue()

            # Open the file for write, write, close
            self.filename=dlg.GetFilename()
            self.dirname=dlg.GetDirectory()
            filehandle=open(os.path.join(self.dirname, self.filename),'w')
            filehandle.write(itcontains)
            filehandle.close()
        # Get rid of the dialog to keep things tidy
        dlg.Destroy()
 
if __name__ == '__main__':
    app= wx.App(0)
    ventana = VentanaHija(None)
    ventana.Show()
    app.MainLoop()

