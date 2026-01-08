"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

import sqlite3

class articuloss():
    def abrir(self):
        conexion=sqlite3.connect("bd1.db")

        return conexion
    def carga(self,datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion,precio) values (?,?)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    def consultas(self,codigo):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select descripcion,precio from articulos where codigo=?"
            cursor.execute(sql,codigo)
            return cursor.fetchall()
            
        finally:
            cone.close()
    def listar(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo,descripcion,precio from articulos"
            cursor.execute(sql)
            
            return cursor.fetchall()
        finally:
            cone.close()
    def borrar(self,codigo):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from articulos where codigo=?"
            cursor.execute(sql,codigo)
            cone.commit()
            return cursor.rowcount

        finally:
            cone.close()
    
    def modificar(self,datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update articulos set descripcion=?, precio=? where codigo=?"
            cursor.execute(sql,datos)
            cone.commit()
            return cursor.rowcount
        finally:
            cone.close()
