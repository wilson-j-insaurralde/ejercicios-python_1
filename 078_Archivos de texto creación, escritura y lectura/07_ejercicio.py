"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear un archivo de texto llamado 'datos.txt' con una codificación utf-8, almacenar tres líneas de texto. Abrir luego el archivo creado con el editor VS Code.
"""

archi1=open("078_Archivos de texto creación, escritura y lectura/datos.txt","w", encoding="utf-8") 
archi1.write("Primer línea.\n") 
archi1.write("Segunda línea.\n") 
archi1.write("Tercer línea.\n")  
archi1.close()