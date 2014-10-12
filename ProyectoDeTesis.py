#! /usr/bin/python
# -*- coding: utf-8 _*_

import wx
from ventanaHija import  VentanaHija

 
class VentanaPrincipal(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, None, wx.NewId(), "Principal",
                          pos=(450,200), size=(450,400))
        try:
            imageName = "tigre.jpeg"
            f = open(imageName, 'rb')
            photo = wx.BitmapFromImage(wx.ImageFromStream(f))        
            wx.StaticBitmap(self, -1, photo)
        except IOError:
            print "Archivo %s no encontrado" % imageName
            raise SystemExit

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.button = wx.Button(self, -1, "Entrar", pos=(350, 250))
        self.SetSizer(self.sizer)
        self.button.Bind(wx.EVT_BUTTON, self.al_botonClick_entrar)
        self.Layout()
 
    def al_botonClick_entrar(self, evt):
        vnt = VentanaHija(self)
        vnt.vntReferente = self
        vnt.vntReferente.Hide()
        vnt.Show()
        

 
if __name__ == '__main__':
    app= wx.App(0)
    ventana = VentanaPrincipal(None)
    ventana.Show()
    app.MainLoop() 
 
    vnt = VentanaHija(self)
    vnt.vntReferente = self