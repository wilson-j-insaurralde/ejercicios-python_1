"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Abrir un archivo de texto con el parámetro "r+", imprimir su contenido actual y agregar luego dos líneas al final."""

archi1=open("078_Archivos de texto creación, escritura y lectura/datos.txt","r+") 
contenido=archi1.read()
print(contenido)
archi1.write("Otra línea 1\n")
archi1.write("Otra línea 2\n")
archi1.close()