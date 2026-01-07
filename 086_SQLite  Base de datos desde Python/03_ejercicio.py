"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Implementaremos un programa que solicite ejecutar un 'select' en la tabla 'articulos' y nos retorne todas sus filas."""


import sqlite3
conexion1=sqlite3.connect("bd1.db")

cursor=conexion1.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)

conexion1.close()