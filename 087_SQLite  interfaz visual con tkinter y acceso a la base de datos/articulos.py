"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

import sqlite3
class articulos:
    def abrir(self):
        conexion1=sqlite3.connect("bd1.db")
        return conexion1
    def alta(self,datos):
        cone=self.abrir()
        cursor=cone.cursor()

        sql="insert into articulos(descripcion,precio) values (?,?)"

        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    def consultar(self,codigo):
       try:
           cone=self.abrir()
           cursor=cone.cursor()
           sql="select descripcion,precio from articulos where codigo=?"
           cursor.execute(sql,codigo)
           return cursor.fetchall()
        
       finally:
           cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo,descripcion,precio from articulos"
            cursor.execute(sql)
            return cursor.fetchall()

        finally:
            cone.close()