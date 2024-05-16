#modulos
import pandas as pd
import csv
import matplotlib.pyplot as plt

#inicio sesion con csv y pandas
def crearusuario():
    with open('usuarios.csv', mode='a', newline="") as file:
        graveler = csv.writer(file, delimiter=",")
        gmail = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")

        # Verificar si el correo electrónico es válido
        if not gmail.endswith("@uvg.edu.gt"):
            print("Correo electrónico inválido. Debe terminar en @uvg.edu.gt")
            return False

        # Verificar si la contraseña es válida
        if len(password) < 8:
            print("Contraseña inválida. Debe contener al menos 8 caracteres")
            return False

        # Agregar una lista vacía como nota inicial
        notas = []

        graveler.writerow([gmail, password, notas])
        print("Usuario registrado con éxito")

def iniciar_sesion():
    gmail = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")

    with open('usuarios.csv', mode='r') as file:
        graveler = csv.reader(file, delimiter=",")
        for row in graveler:
            if row[0] == gmail and row[1] == password:
                print("Sesión iniciada con éxito")
                return True
        print("Correo electrónico o contraseña incorrectos")
        return False

#funcion para ver perfil
def verperfil(gmail):
    if iniciar_sesion():
        with open('usuarios.csv', mode='r') as file:
            graveler = csv.reader(file, delimiter=",")
            for row in graveler:
                if row[0] == gmail:
                    print("Correo electrónico: ", row[0])
                    break

#funcion para validar correo
def validarcorreo(gmail):
    with open('usuarios.csv', mode='r') as file:
        graveler = csv.reader(file, delimiter=",")
        for row in graveler:
            if row[0] == gmail:
                return True
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------
#funcion para registrar notas
def registrarnotas(gmail):
    usuario = input("Ingrese el correo del usuario: ")
    nota = input("Ingrese la nota: ")
    # Leer los usuarios en una lista
    with open('usuarios.csv', mode='r') as file:
        graveler = csv.reader(file, delimiter=",")
        usuarios = list(graveler)

    # Agregar la nota al usuario correspondiente
    for usuario in usuarios:
        if usuario[0] == gmail:
            # Convertir la cadena de notas en una lista
            notas = eval(usuario[2])
            # Agregar la nueva nota a la lista
            notas.append(nota)
            # Convertir la lista de notas en una cadena
            usuario[2] = str(notas)

    # Escribir los usuarios de vuelta al archivo
    with open('usuarios.csv', mode='w', newline="") as file:
        graveler = csv.writer(file, delimiter=",")
        graveler.writerows(usuarios)

#editar notas
def editarnotas(gmail):
    if iniciar_sesion():
        with open('usuarios.csv', mode='r') as file:
            graveler = csv.reader(file, delimiter=",")
            usuarios = list(graveler)
            notas = []
            for row in usuarios:
                if row[0] == gmail:
                    notas = eval(row[2])
                    break
            print("Notas: ")
            for i, nota in enumerate(notas, start=1):
                print(f"{i}. {nota}")
            nota_a_editar = int(input("Ingrese el número de la nota que desea editar: "))
            if 1 <= nota_a_editar <= len(notas):
                nueva_nota = input("Ingrese la nueva nota: ")
                notas[nota_a_editar - 1] = nueva_nota
                print("Nota editada con éxito")
            else:
                print("Número de nota inválido")
        with open('usuarios.csv', mode='w', newline="") as file:
            graveler = csv.writer(file, delimiter=",")
            for row in usuarios:
                if row[0] == gmail:
                    row[2] = str(notas)
            graveler.writerows(usuarios)

#eliminar notas
def eliminarnotas(gmail):
    if iniciar_sesion():
        with open('usuarios.csv', mode='r') as file:
            graveler = csv.reader(file, delimiter=",")
            usuarios = list(graveler)
            notas = []
            for row in usuarios:
                if row[0] == gmail:
                    notas = eval(row[2])
                    break
            print("Notas: ")
            for i, nota in enumerate(notas, start=1):
                print(f"{i}. {nota}")
            nota_a_eliminar = int(input("Ingrese el número de la nota que desea eliminar: "))
            if 1 <= nota_a_eliminar <= len(notas):
                del notas[nota_a_eliminar - 1]
                print("Nota eliminada con éxito")
            else:
                print("Número de nota inválido")
        with open('usuarios.csv', mode='w', newline="") as file:
            graveler = csv.writer(file, delimiter=",")
            for row in usuarios:
                if row[0] == gmail:
                    row[2] = str(notas)
            graveler.writerows(usuarios)

def vernotas(gmail):
    if iniciar_sesion():
        with open('usuarios.csv', mode='r') as file:
            graveler = csv.reader(file, delimiter=",")
            usuarios = list(graveler)
            notas = []
            for row in usuarios:
                if row[0] == gmail:
                    notas = eval(row[2])
                    break
            print("Notas: ")
            for i, nota in enumerate(notas, start=1):
                print(f"{i}. {nota}")

def notasmenu(gmail):
    if iniciar_sesion():
        opcion = '0'
        while opcion != '5':
            print("1. Registrar notas")
            print("2. Editar notas")
            print("3. Eliminar notas")
            print("4. Ver notas")
            print("5. Salir")
            opcion = input("Ingrese la opción: ")
            if opcion == '1':
                registrarnotas(gmail)
            elif opcion == '2':
                editarnotas(gmail)
            elif opcion == '3':
                eliminarnotas(gmail)
            elif opcion == '4':
                verperfil(gmail)
            elif opcion == '5':
                return
            else:
                print("Opción inválida")

#--------------------------------------------------------------------------------------------------------------------------------------------------
#funciones de pandas 1-10

#Mostrar al usuario la cantidad de sismos que han ocurrido en los últimos 5 años y los nombres de las variables que comprenden el conjunto de datos
def sismos5():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    print("Cantidad de sismos en los últimos 5 años: ", sismos.shape[0])
    print("Variables: ", sismos.columns)

#Mostrar cuantos sismos han ocurrido en el año n. El n lo ingresa el usuario.
def sismosn():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    n = int(input("Ingrese el año: "))
    sismosn = sismos[sismos["Anio"] == n]
    print("Cantidad de sismos en el año ", n, ": ", sismosn.shape[0])

#Mostrar los primeros 10 sismos ocurridos en el territorio nacional en el año seleccionado por el usuario
def sismos10():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    n = int(input("Ingrese el año: "))
    sismosn = sismos[sismos["Anio"] == n]
    print(sismosn.head(10))

#Mostrar los n primeros sismos de menor intensidad. El n lo debe ingresar el usuario.
def sismosnintensidad():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    n = int(input("Ingrese la cantidad de sismos: "))
    sismosn = sismos.sort_values("MAG")
    print(sismosn.head(n))

#Mostrar los 10 sismos que fueron detectados por el menor número de estaciones en el año n. El n lo ingresa el usuario
def sismos10estaciones():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    n = int(input("Ingrese el año: "))
    sismosn = sismos[sismos["Anio"] == n]
    sismosn = sismosn.sort_values("NST")
    print(sismosn.head(10))

#Mostrar cual ha sido la magnitud promedio de los sismos en un año x, que ingrese el usuario
def sismospromedio():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    n = int(input("Ingrese el año: "))
    sismosn = sismos[sismos["Anio"] == n]
    print("Magnitud promedio: ", sismosn["MAG"].mean())

#Mostrar el promedio de la magnitud y profundidad de los sismos por mes. ¿En qué meses se producen los sismos de menor intensidad? Debe dar la opción de ver la información gráficamente, el usuario debe seleccionar si quiere ver la gráfica de magnitud o de profundidad.
def sismosmes():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    sismos["Mes"] = pd.to_datetime(sismos["TiempodeOrigen"]).dt.month
    sismosmes = sismos.groupby("Mes").agg({"MAG": "mean", "Profundidad": "mean"})
    print(sismosmes)
    grafica = input("¿Desea ver la gráfica? (s/n): ")
    if grafica.lower() == "s":
        grafico = input("¿Magnitud o profundidad? ")
        if grafico.lower() == "magnitud":
            sismosmes["MAG"].plot(kind="bar")
            plt.show()
        elif grafico.lower() == "profundidad":
            sismosmes["Profundidad"].plot(kind="bar")
            plt.show()

#Mostrar cuantos sismos sensibles han ocurrido en promedio por año. El sistema debe dar la opción de visualizar una gráfica
def sismossensibles():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    sismossensibles = sismos[sismos["Sensible"] == "si"]
    sismossensibles = sismossensibles.groupby("Anio").size()
    print("Sismos sensibles por año: ", sismossensibles.mean())
    grafica = input("¿Desea ver la gráfica? (s/n): ")
    if grafica.lower() == "s":
        sismossensibles.plot(kind="bar")
        plt.show()

#Mostrar cuantos sismos por año tienen un error mayor a 25kms en su localización
def sismoserror():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    sismoserror = sismos[sismos["No"] >= 25]
    # Contar cuántos sismos tienen un error de localización mayor a 25 kms por año
    conteo_sismos = sismoserror.groupby(sismoserror['TiempodeOrigen'].dt.year).size()
    print("Sismos con error mayor a 25kms por año: ", conteo_sismos)

# Mostrar toda la información del sismo que ha tenido la menor cantidad de fases hasta el momento
def sismosfases():
    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    sismosfases = sismos.nsmallest(1, "NF")
    print("El sismo con menor cantidad de fases es", sismosfases)

#----------------------extras----------------------------------------------------------------
#Mostrar cuantos sismos sensibles por día del mes han ocurrido en promedio. ¿Tiembla más al inicio, medio o fin de mes?
def sismosdiames():
    # Leer los sismos
    df = pd.read_csv("reporte_sismos_2019_2023.csv")
    # Filtrar los sismos sensibles
    sismos_sensibles = df[df['Sensible'] == 'si']

    # Contar cuántos sismos sensibles han ocurrido en promedio por día del mes
    conteo_sismos = sismos_sensibles.groupby(sismos_sensibles['TiempodeOrigen'].dt.day).size()

    print(conteo_sismos)
    print("Promedio de sismos sensibles por día del mes: ", conteo_sismos.mean())

#Mostrar un mapa con los sismos registrados en un año seleccionado por el usuario. Puede usar Geopandas para esto. Se le suministra el archivo .shp con los departamentos de Guatemala
def sismosmapa():
    import geopandas as gpd
    import fiona
    import os

    os.environ["SHAPE_RESTORE_SHX"] = "YES"

    sismos = pd.read_csv("reporte_sismos_2019_2023.csv")
    n = int(input("Ingrese el año: "))
    sismosn = sismos[sismos["Anio"] == n]
    departamentos = gpd.read_file("departamentos_gtm.shp")
    #lugares:nacional,
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    departamentos.boundary.plot(ax=ax)
    sismosn.plot(ax=ax, color="red", markersize=5)
    plt.show()
