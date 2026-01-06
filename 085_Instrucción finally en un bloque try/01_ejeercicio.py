"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Almacenar una serie de string en un archivo de texto. Tratar de llamar al método 'write' pasando un entero
"""

try: 
    archi1=open("085_Instrucción finally en un bloque try/datos.txt","w")
    archi1.write("primera linea.\n")
    archi1.write("segunda linea.\n")
    archi1.write("tercera linea.\n")
    archi1.write(3334)


except TypeError:
    print("No se puede grabar un entero con write") 
finally:
    archi1.close()
    print("se cerrro el archivo")