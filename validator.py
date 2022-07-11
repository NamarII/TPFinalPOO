# -*- coding: utf-8 -*-

from db import dba
from validate_email import validate_email
import base64
from dataclasses import asdict


class Validator():
    
    def __init__(self):
        pass
    
    def validar_usuario(self,dicc):
        datosFinales={}
        errores={}
        caracteresEspeciales=['$','@','#','%']
        
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        
        if datosFinales['nombre']=='':
            errores['nombre']='Campo nombre vacio'
            
        if datosFinales['apellido']=='':
            errores['apellido']='Campo apellido vacio'
            
        if datosFinales['domicilio']=='':
            errores['domicilio']='Campo domicilio vacio'
            
        if datosFinales['DNI']=='':
            errores['DNI']='Campo DNI vacio'
            
        if datosFinales['Fecha_nac']=='':
            errores['Fecha_nac']='Campo Fecha_nac vacio'
            
        if datosFinales['mail']=='':
            errores['mail']='Campo mail vacio'
            
        elif validate_email(datosFinales['mail'])==False:
            errores['mail']='No tiene formato de mail'
        
        if datosFinales['password']=='':
            errores['password']='Campo password vacio'
        elif len(datosFinales['password'])<6:
            errores['password']='La password debe tener al menos 6 caracteres'
        elif not any(i.isupper() for i in datosFinales['password']):
            errores['password']='La password debe tener al menos 1 caracter con mayuscula'
        elif not any(i.islower() for i in datosFinales['password']):
            errores['password']='La password debe tener al menos 1 caracter con minuscula'
        elif not any(i in caracteresEspeciales  for i in datosFinales['password']):
            errores['password']='La password debe tener al menos 1 caracter con especial'
        elif datosFinales['password']!=datosFinales['cpassword']:
            errores['password']='la password no coincide'
    
    def validar_producto(self,dicc):
        datosFinales={}
        errores={}
        for x,y in dicc.items():
            datosFinales[x]=y.strip()  
        if datosFinales['marca']=='':
            errores['marca']='Campo marca vacio'
            print(errores)
        elif datosFinales['modelo']=='':
            errores['modelo']='Campo modelo vacio'
            print(errores)
        elif datosFinales['proveedor']=='':
            errores['proveedor']='Campo proveedor vacio'
            print(errores)
        elif datosFinales['precio']=='':
            errores['precio']='Campo precio vacio'
            print(errores)
        elif datosFinales['precio'].isdigit()==False:
            errores['precio']='El precio contiene un caracter'
            print(errores)
        elif errores=={}:
            sql='SELECT * FROM celular where numero = %s'
            val=(datosFinales['numero'],)
            dba.get_cursor().execute(sql,val)
            dba.get_conexion().commit
            dba.get_cursor().fetchone()
            result=dba.get_cursor().fetchone()
            if result is not None:
                errores['numero']='El numero existe en el sistema'
                print(errores)
            else:
                return True
        else:
            return True
    
    def validar_login(self,dicc):
        
        datosFinales={}
        errores={}
        
        for x,y in dicc.items():
            datosFinales[x]=y.strip()
        
        sql="select * from usuario where mail=%s"
        val=(datosFinales['mail'],)
        dba.get_cursor().execute(sql,val)
        dba.get_conexion().commit
        
        result=dba.get_cursor().fetchone()
        
       # print(base64.decodebytes(result[0].encode("UTF-8")).decode('utf-8'))
        
        if result is None:
            errores['mail']="el mail ingresado no existe en la base"
            return errores
        
        elif base64.decodebytes(result[7].encode("UTF-8")).decode('utf-8')!=datosFinales['password']:
            errores['password']='La password es incorrecta'
            return errores
            # return base64.decodebytes(result[0].encode("UTF-8")).decode('utf-8')
        else:
            return result

val=Validator()
        
        
            
        
            