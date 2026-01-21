"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""Lectura de una página HTML."""

from urllib import request

pagina=request.urlopen("https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=99&codigo=100&inicio=90")
datos=pagina.read()
datosutf8=datos.decode("utf-8")
print(datosutf8)