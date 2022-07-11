# -*- coding: utf-8 -*-

from validator import val 
#from producto import Producto
from usuario import Usuario
from compras import Compras
#from dataclasses import asdict
from db import dba
import sys
    
    
def menu_app():
    print("Bienvenido a la aplicacion ")
    print("-------------------------- \n")
    
    opcion=int(input("Elija las siguientes opciones \n Opcion 1: Registracion  \n Opcion 2: Iniciar Sesion \n Opcion 3: Salir de la aplicacion \n"))
    if opcion==1:
        #usuario=registracion_usuario()
        print("Bienvenido a la registracion del usuario")
        print("----------------------------------------- \n")
        registracion_usuario()
        #if val.validar_login(login)==login['password']:
            #print('Se ha logueado correctamente')
            #menu_usuario()
        #else:
            #print('Contraseña incorrecta')
    elif opcion == 2:
        login()
    else:
        sys.exit()

def registracion_usuario():
    i = False
    while not i == True:
        usuario={}
        usuario['nombre']=input('ingrese nombre: \n')
        usuario['apellido']=input('ingrese apellido: \n')
        usuario['domicilio']=input('ingrese domicilio: \n')
        usuario['DNI']=input('ingrese DNI: \n')
        usuario['Fecha_nac']=input('ingrese fecha de nacimiento: \n')
        usuario['mail']=input('ingrese mail: \n')
        usuario['password']=input('ingrese password: \n')
        usuario['cpassword']=input('ingrese de nuevo la password: \n')
        errores=val.validar_usuario(usuario)
        if val.validar_usuario(usuario) == True:
            del usuario['cpassword']
            usuario1=Usuario(**usuario)
            usuario1.save()
            print('Su usuario se agrego exitosamente.')
            menu_usuario(usuario1)

        if not errores:
            del usuario['cpassword']
            usuario1=Usuario(**usuario)
            usuario1.save()
            print('su usuario se agrego exitosamente')
            return usuario1
            for i in errores.values():
                print(i)

def login():
    login={}

    login['mail']=input('ingrese su mail: ')
    login['password']=input('ingrese su password: ')
    result = val.validar_login(login)
    if type(result)==tuple:
        print('Se ha logueado correctamente')
        print('****************************\n')
        usuario1=Usuario(result[1], result[2], result[3], result[4], result[5], result[6], result[7],)
        usuario1.set_id(result[0])
        menu_usuario(usuario1)
                
    else:
       print('Error al loguearse')
       print('******************\n')
       menu_app()
   
def menu_usuario(usuario1):
    print(' Elija entre las siguientes opciones. \n')
    print('1: Modificar datos de usuario.')
    print('2: Comprar producto.')
    print('3: Cerrar sesion.')
    print('4: Cerrar aplicacion.')
    opcion = int(input('Ingrese su opción: \n'))
    if opcion == 1:
        print('Elija que dato desea modificar: ')
        print(' Opcion 1: Modificar el nombre \n')
        print(' Opcion 2: Modificar el apellido \n')
        print(' Opcion 3: Modificar el domicilio \n')
        print(' Opcion 4: Modificar el DNI \n')
        print(' Opcion 5:Modificar la fecha de nacimiento \n')
        print(' Opcion 6:Modificar el email \n')
        print(' Opcion 7:Modificar la password \n')
        print(' Opcion 8: Eliminar el usuario del sistema \n')
        print(' Opcion 9:Volver al menu principal \n')
        opcion=int(input ('INGRESE LA OPCIÓN: '))
        if opcion==1:
            nombre=input("ingrese el nombre: ")
            usuario1.update_nombre(nombre)
            print("se modifico correctamente el nombre")
            menu_usuario(usuario1)
        elif opcion==2:
            apellido=input("ingrese el apellido: ")
            usuario1.update_apellido(apellido)
            print("se modifico correctamente el apellido")
            menu_usuario(usuario1)
        elif opcion==3:
            domicilio=int(input("ingrese el domicilio: "))
            usuario1.update_domicilio(domicilio)
            print("se modifico correctamente el domicilio")
            menu_usuario(usuario1)
        elif opcion==4:
            DNI=int(input("ingrese el DNI: "))
            usuario1.update_DNI(DNI)
            print("se modifico correctamente el DNI")
            menu_usuario(usuario1)
        elif opcion==5:
            Fecha_nac=int(input("ingrese la fecha de nacimiento: "))
            usuario1.update_Fecha_nac(Fecha_nac)
            print("se modifico correctamente la fecha de nacimiento")
            menu_usuario(usuario1)
        elif opcion==6:
            mail=int(input("ingrese el mail: "))
            usuario1.update_mail(mail)
            print("se modifico correctamente el e-mail")
            menu_usuario(usuario1)
        elif opcion==7:
            password=int(input("ingrese la password: "))
            usuario1.update_password(password)
            print("se modifico correctamente el password")
            menu_usuario(usuario1)
        elif opcion==8:
            sql="delete from usuarios where mail = %s"
            val=(login["mail"],)
            dba.get_cursor().execute(sql,val)
            dba.get_conexion().commit()
            print("El usuario ha sido eliminado con exito.")
            menu_app()
        else:
            menu_app()
    
    elif opcion == 2:
        dba.get_cursor().execute('select * from producto')
        dba.get_conexion().commit
        result = dba.get_cursor().fetchall()
        for x in result:
            print(x)
        opcion = int(input('Elija un producto: \n'))
        i = False
        while not i == True:
            compras={}
            compras["id_usuario"] = usuario1.get_id()
            compras["Producto_id"] = opcion
            compra1=Compras(**compras)
            compra1.save()
            print("Su compra se ha realizado con exito.")
            i = True
            menu_usuario(usuario1)
    elif opcion == 3:
        menu_app()
    elif opcion ==4:
        quit()
    else:
        print("La opcion es incorrecta.")
        menu_usuario(usuario1)
    
menu_app()        
    





    








