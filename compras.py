# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:33:19 2022

@author: Namar_II
"""

from db import dba

class Compras():
    def __init__(self,id_usuario,Producto_id):
        self.__ids=0
        self.__id_usuario=id_usuario
        self.__Producto_id=Producto_id
    
    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_Producto_id(self):
        return self.__Producto_id
    
    def set_id_usuario(self,id_usuario):
        self.__id_usuario=id_usuario
    
    def set_Producto_id(self,Producto_id):
        self.__Producto_id=Producto_id

    def get_id(self):
        return self.__ids
    
    def set_id(self,ids):
        self.__ids=ids
    
    def save(self):
        sql=' insert into Compras (id_usuario, Producto_id) values(%s,%s)'
        val=(self.__id_usuario,self.__Producto_id)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
        
    def eliminar_producto(self):
        sql="delete from compras where  id_usuario=%s"
        val=(self,)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()