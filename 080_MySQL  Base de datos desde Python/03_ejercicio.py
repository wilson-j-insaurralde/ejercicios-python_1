"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Ahora implementaremos un programa que inserte un par de filas en la tabla 'articulos'.

"""
import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")
cursor1=conexion1.cursor()
sql="insert into articulos (descripcion, precio) values (%s,%s)"

datos=("naranja",23.50)
cursor1.execute(sql,datos)
datos=("peras",34)

cursor1.execute(sql, datos)
datos=("bananas", 25)
cursor1.execute(sql,datos)
conexion1.commit()
conexion1.close()