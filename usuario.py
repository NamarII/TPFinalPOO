# -*- coding: utf-8 -*-

from db import dba
import base64
from validate_email import validate_email

class Usuario():
    
    def __init__(self,nombre,apellido, domicilio, mail, DNI, Fecha_nac, password):
        self.__id=0
        self.__nombre=nombre
        self.__apellido=apellido
        self.__domicilio=domicilio
        self.__mail=mail
        self.__DNI=DNI
        self.__Fecha_nac=Fecha_nac
        self.set_password(password)
        
    def get_id(self):
        return self.__ids
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido

    def get_domicilio(self):
        return self.__domicilio
    
    def get_mail(self):
        return self.__mail
    
    def get_password(self):
        return self.__password
    
    def get_DNI(self):
        return self.__DNI
    
    def get_Fecha_nac(self):
        return self.__Fecha_nac
    
    def set_id(self,ids):
        self.__ids=ids
        
    def set_nombre(self,nombre):
        self.__nombre=nombre
    
    def set_apellido(self,apellido):
        self.__apellido=apellido
        
    def set_domicilio(self,domicilio):
        self.__domicilio=domicilio
    
    def set_mail(self,mail):
        self.__mail=mail
        
    def set_DNI(self,DNI):
        self.__DNI=DNI
        
    def set_Fecha_nac(self,Fecha_nac):
        self.__Fecha_nac=Fecha_nac
    
    def set_password(self,password):
        self.__password=self.encriptarPass(password)
    
    def encriptarPass(self, password):
        return base64.encodebytes(bytes(password, 'utf-8')).decode('utf-8')
    
    def desencriptarPass(self,password):
        return base64.decodebytes(password.encode("UTF-8")).decode('utf-8')
    
    def save(self):
        sql='insert into usuario ( nombre, apellido, domicilio, mail, DNI, Fecha_nac, password) values (%s, %s, %s, %s, %s, %s, %s)'
        val=(self.get_nombre(), self.get_apellido(), self.get_domicilio(), self.get_mail(), self.get_DNI(), self.get_Fecha_nac(), self.get_password())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        
    #def delete(self):
       # sql='delete from usuario where ID_Usuario=%s'
       # val=(self.get_id(),)
        #dba.get_cursor().execute(sql,val)
       # dba.get_conexion().commit()
    
    def update_nombre(self, nombre):
        sql='update usuario set nombre=%s where ID_Usuario=%s '
        val=(nombre, self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
    
    def update_apellido(self, apellido):
         sql='update usuario set apellido=%s where ID_Usuario=%s '
         val=(apellido, self.__ids)
         dba.get_cursor().execute(sql,val)
         dba.get_conexion().commit()
         self.set_id(dba.get_cursor().lastrowid)
    
    def update_domicilio(self, domicilio):
        sql='update usuario set domicilio=%s where ID_Usuario=%s '
        val=(domicilio, self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
        self.set_id(dba.get_cursor().lastrowid)
    
    def update_mail(self, mail):
        sql='update usuario set mail=%s where ID_Usuario=%s '
        val=(mail, self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()

    def update_password(self,password):
        sql='update usuario set password=%s where ID_Usuario=%s '
        val=(password,self.__ids)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    def update_DNI(self, DNI):
         sql='update usuario set DNI=%s where ID_Usuario=%s '
         val=(DNI, self.__ids)
         dba.get_cursor().execute(sql,val)
         dba.get_conexion().commit()
         self.set_id(dba.get_cursor().lastrowid)
    
    def update_Fecha_nac(self, Fecha_nac):
         sql='update usuario set Fecha_nac=%s where ID_Usuario=%s '
         val=(Fecha_nac, self.__ids)
         dba.get_cursor().execute(sql,val)
         dba.get_conexion().commit()
         self.set_id(dba.get_cursor().lastrowid)
    
    def mostrar_datos_comprador(self):
        sql= "select * from usuario where mail=%s"
        val= (self.get_mail())
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit()
    
    