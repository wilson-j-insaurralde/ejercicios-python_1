"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Implementaremos un programa que solicite el ingreso de un precio y luego nos muestre la descripción de todos los artículos con un precio inferior al ingresado.
"""

import sqlite3 

precio=float(input("ingrese el precio deseado: "))

conexion1=sqlite3.connect("bd1.db")
cursor=conexion1.execute("select codigo,descripcion,precio from articulos where precio<?",(precio,))
filas=cursor.fetchall()

if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("no existen articulos con precio menor al ingresado.")
conexion1.close()