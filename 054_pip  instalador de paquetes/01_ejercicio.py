"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""pip install wxPython"""
"""Codificaremos un programa mínimo que muestre una ventana con el mensaje "Hola Mundo" empleando el paquete wxPython:"""

import wx

aplicacion=wx.App()
ventana=wx.Frame(parent=None,title="holiiiiiiiiii")
ventana.Show()
aplicacion.MainLoop()

# documentacion: https://wiki.wxpython.org/How%20to%20Learn%20wxPython