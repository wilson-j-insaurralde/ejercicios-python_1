"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Leer el contenido del archivo de texto 'datos.txt' y almacenar sus líneas en una lista. Imprimir la cantidad de líneas que tiene el archivo y su contenido"""

archi1=open("078_Archivos de texto creación, escritura y lectura/datos.txt","r")
lineas1=archi1.readlines()
print('el archivo tiene',len(lineas1),'lineas')
print('El contenido del archivo')
for linea in lineas1:
    print(linea,end='')
archi1.close()
