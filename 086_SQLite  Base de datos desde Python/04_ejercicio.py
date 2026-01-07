
"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Implementaremos un programa que solicite el ingreso del código de un producto y luego nos muestre su descripción y precio.
"""

import sqlite3

conexion1=sqlite3.connect("bd1.db")

codigo=int(input("ingrese el codigo de un articulo: "))
cursor=conexion1.execute("select descripcion,precio from articulos where codigo=?",(codigo,))
fila=cursor.fetchone()

if fila !=None:
    print(fila)

else:
    print("no existe un articulo con dicho codigo")

conexion1.close()

