"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Borrar una base de datos.
Cuando queremos crear una base de datos que ya existe se genera un error, podemos primero borrarla y luego ya si crearla sin problemas.
"""
import mysql.connector

conexion1=mysql.connector.connect(host="localhost",user="root",passwd="")

cursor1=conexion1.cursor()

sql="drop database if exists bd2"
cursor1.execute(sql)

sql="create database bd2"
cursor1.execute(sql)
sql="use bd2"
cursor1.execute(sql)
sql="""create table usuarios(
            nombre varchar(30) primary key,
            clave varchar (30)
    )"""
cursor1.execute(sql)
conexion1.commit()
conexion1.close()