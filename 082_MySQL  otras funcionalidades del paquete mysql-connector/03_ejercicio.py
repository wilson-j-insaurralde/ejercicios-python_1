"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
En conceptos anteriores vimos como crear una base de datos de MySQL utilizando la aplicación PHPMyAdmin, en algunas situaciones podemos necesitar crear una base de datos desde el mismo programa de Python. La misma metodología será si queremos crear tablas.
"""
import mysql.connector

conexion1=mysql.connector.connect(host="localhost",user="root",passwd="")


cursor1=conexion1.cursor()

sql="create database bd2"
cursor1.execute(sql)

sql="use bd2"
cursor1.execute(sql)
sql=("""create table usuarios(
        nombre varchar(30) primary key,
        clave varchar(30))
     """)
cursor1.execute(sql)
conexion1.commit()
conexion1.close()