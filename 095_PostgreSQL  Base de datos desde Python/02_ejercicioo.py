"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Implementaremos un programa que solicite ejecutar un 'select' en la tabla 'articulos' de la base de datos 'bd1' y nos retorne todas sus filas.
"""

import psycopg2

conexion1=psycopg2.connect(database="bd1",user="postgres",password="66112233")
cursor1=conexion1.cursor()

sql="select * from articulos"

cursor1.execute(sql)
for fila in cursor1:
    print(fila)

conexion1.close() 