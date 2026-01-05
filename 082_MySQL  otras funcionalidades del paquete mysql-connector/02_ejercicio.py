"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
La clase cursor a parte del método 'execute' cuenta con otro método llamado 'executemany' que tiene el objetivo de insertar múltiples filas de una tabla.
"""
import mysql.connector

conexion1=mysql.connector.connect(host="localhost",user="root",passwd="",database="bd1")

cursor1=conexion1.cursor()
sql="insert into articulos (descripcion,precio) values (%s,%s)"
filas=[
    ("naranjas", 23.50),
    ("bananas", 34),
    ("peras", 21),
    ("sandía", 19.60)
    ]

cursor1.executemany(sql, filas)
conexion1.commit()
conexion1.close()