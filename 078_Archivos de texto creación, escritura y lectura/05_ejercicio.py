"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Abrir el archivo de texto 'datos.txt' y luego agregar 2 líneas. Imprimir luego el archivo completo."""

archi1=open("078_Archivos de texto creación, escritura y lectura/datos.txt","a")

archi1.write("nueva linea 1\n")
archi1.write("nueva linea 2\n")
archi1.close()
archi1=open("078_Archivos de texto creación, escritura y lectura/datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()
