"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Leer el contenido del archivo de texto 'datos.txt' línea a línea.
"""
archi1=open("078_Archivos de texto creación, escritura y lectura/datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea,end='')
    linea=archi1.readline()
archi1.close()
