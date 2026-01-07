"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Ahora implementaremos un programa que inserte un par de filas en la tabla 'articulos' de la base de datos 'bd1' que acabamos de crear con el programa anterior.
"""

import sqlite3

conexion1=sqlite3.connect("bd1.db")
conexion1.execute("insert into articulos (descripcion,precio) values (?,?)",("naranjas",23.50))

conexion1.execute("insert into articulos (descripcion,precio) values (?,?)",("peras",34))
conexion1.execute("insert into articulos (descripcion,precio) values (?,?)",("bananas",25))
conexion1.commit()
conexion1.close()