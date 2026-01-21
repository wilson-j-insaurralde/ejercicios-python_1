"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Lectura de una página HTML u otro recurso y posterior grabación del archivo en forma local.
Recuperar la página html 'pagina1.html' y el archivo 'imagen1.jpg' que se encuentran localizados en:

http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html
http://www.scratchya.com.ar/pythonya/ejercicio336/imagen1.jpg
luego grabar los dos archivos en forma local en el equipo donde se está ejecutando el script de Python.
"""


from urllib import request

pagina=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/pagina1.html")
datos=pagina.read()
archivo1=open("pagina1.html","wb")
archivo1.write(datos)
archivo1.close()

imagen=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/imagen1.jpg")
datos=imagen.read()
archivo2=open("imagen1.jpg","wb")
archivo2.write(datos)
archivo2.close()

