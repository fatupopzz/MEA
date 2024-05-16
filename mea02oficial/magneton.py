#modulos 
import pandas as pd
import csv
import matplotlib.pyplot as plt
import magnemite as mg



#iniciar o regustrar usuario
def menu():
    print("1. Iniciar sesión")
    print("2. Crear usuario")
    print("3. Salir")
    opcion = input("Ingrese la opción: ")
    if opcion == '1':
        #verificar correo y contraseña
        if mg.iniciar_sesion() == False:
            return
        #si inicia sesion, se llama al menu de funciones
        else:
            menufunciones()
    elif opcion == '2':
        if mg.crearusuario() == False:
            return
        else:
            menufunciones()
    elif opcion == '3':
        return
    else:
        print("Opción inválida")


#menu para llamar a todas las funciones
def menufunciones():
    opcion = '0'
#estas son las opciones
    while opcion != '15':
        print("1. Cantidad de sismos en los últimos 5 años")
        print("2. Cantidad de sismos en un año")
        print("3. Primeros 10 sismos en un año")
        print("4. Primeros n sismos de menor intensidad")
        print("5. 10 sismos con menor número de estaciones en un año")
        print("6. Magnitud promedio en un año")
        print("7. Promedio de magnitud y profundidad por mes")
        print("8. Sismos sensibles por año")
        print("9. Sismos con error mayor a 25kms")
        print("10. Sismo con menor cantidad de fases")
        print("11. Sismos sensibles por día del mes")
        print("12. Mapa de sismos en un año")
        print("13. Ver perfil")
        print("14. Notas de sismos")
        print("15. Salir")
        opcion = input("Ingrese la opción: ")
        if opcion == '1':
            mg.sismos5()
        elif opcion == '2':
            mg.sismosn()
        elif opcion == '3':
            mg.sismos10()
        elif opcion == '4':
            mg.sismosnintensidad()
        elif opcion == '5':
            mg.sismos10estaciones()
        elif opcion == '6':
            mg.sismospromedio()
        elif opcion == '7':
            mg.sismosmes()
        elif opcion == '8':
            mg.sismossensibles()
        elif opcion == '9':
            mg.sismoserror()
        elif opcion == '10':
            mg.sismosfases()
        elif opcion == '11':
            mg.sismosdiames()
        elif opcion == '12':
            mg.sismosmapa()
        elif opcion == '13':
            gmail = input("Ingrese el correo al que desea enviar el perfil: ")
            #revisar si el correo es valido
            if mg.validarcorreo(gmail) == False:
                print("Correo inválido")
            else:
                mg.verperfil(gmail)
        elif opcion == '14':
            gmail = input("Ingrese el correo al que desea enviar las notas: ")
            #revisar si el correo es valido
            if mg.validarcorreo(gmail) == False:
                print("Correo inválido")
            else:
                mg.notasmenu(gmail)
        elif opcion == '15':
            return
        else:
            print("Opción inválida")
menu()