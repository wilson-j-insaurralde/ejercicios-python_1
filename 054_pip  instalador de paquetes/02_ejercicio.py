"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mostrar una ventana con un botón en su interior. Al ser presionado mostrar un mensaje.

El programa en Python haciendo uso del paquete wxPython requiere el siguiente algoritmo:
"""
import wx

class ventana (wx.Frame):
    def __init__ (self,*args,**kw):
        super(ventana,self).__init__(*args,**kw)
        self.boton1=wx.Button(self, label="presionar")
        self.Bind(wx.EVT_BUTTON, self.presion_boton,self.boton1)
    def presion_boton(self,evento):
        wx.MessageBox("hola mundo")
aplicacion= wx.App()
frm= ventana(None, title="prueba")
frm.Show()
aplicacion.MainLoop()
