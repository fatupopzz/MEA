import csv
import pandas as pd
import matplotlib.pyplot as plt


# variable
opcion = 0

#leer archivo de usuario
usuario = pd.read_csv('usuarios.csv')

# leer archivo csv
df = pd.read_csv('reporte_sismos_2019_2023.csv')

# Convertir la columna "TiempodeOrigen" a un tipo de dato de fecha y hora
df['TiempodeOrigen'] = pd.to_datetime(df['TiempodeOrigen'])

# Crear una nueva columna "Mes" que contiene el mes de la fecha
df['Mes'] = df['TiempodeOrigen'].dt.month

#def de todo porq si
def anos5():
    print("Cantidad de sismos en los últimos 5 años: ", df.shape[0])
    print("Nombres de las variables: ", df.columns)

def mostrar_sismos_anio(anio):
    print(df[df['Anio'] == anio])

def mostrar_primeros_10_territorio_nacional(anio):
    print(df[(df['Anio'] == anio) & (df['ZS'] == 'Nacional')].head(10))

def mostrar_n_primeros_menor_intensidad(n):
    print(df.nsmallest(n, 'MAG'))

def mostrar_10_sismos_menor_estaciones(anio):
    print(df[df['Anio'] == anio].nsmallest(10, 'NST'))

def promediomagnitud(anio):
    print("Promedio de magnitud: ", df[df['Anio'] == anio]['MAG'].mean())

def mostrar_promedio_magnitud(mes):
    # Calcular el promedio de magnitud y profundidad por mes
    promedios = df.groupby('Mes')[['MAG', 'Profundidad']].mean()

    # Encontrar el mes con la menor magnitud promedio
    mes_menor_magnitud = promedios['MAG'].idxmin()

    print("El mes con los sismos de menor intensidad es:", mes_menor_magnitud)

    # Preguntar al usuario si quiere ver la gráfica
    ver_grafica = input("¿Quieres ver la gráfica de magnitud o de profundidad? (magnitud/profundidad): ")

    if ver_grafica.lower() == 'magnitud':
        promedios['MAG'].plot(kind='bar')
        plt.title('Promedio de magnitud de sismos por mes')
        plt.xlabel('Mes')
        plt.ylabel('Magnitud promedio')
        plt.show()
    elif ver_grafica.lower() == 'profundidad':
        promedios['Profundidad'].plot(kind='bar')
        plt.title('Promedio de profundidad de sismos por mes')
        plt.xlabel('Mes')
        plt.ylabel('Profundidad promedio')
        plt.show()
    else:
        print("Opción no válida")


def mostrar_sismos_sensibles():
    # Filtrar los sismos sensibles
    sismos_sensibles = df[df['Sensible'] == 'S']

    # Contar cuántos sismos sensibles han ocurrido en promedio por año
    conteo_sismos = sismos_sensibles.groupby(sismos_sensibles['TiempodeOrigen'].dt.year).size()

    print(conteo_sismos)
    

def mostrar_sismos_error_localizacion():
    # Filtrar los sismos con un error de localización mayor a 25 kms
    sismos_error_mayor_25 = df[df['No'] >= '25']

    # Contar cuántos sismos tienen un error de localización mayor a 25 kms por año
    conteo_sismos = sismos_error_mayor_25.groupby(sismos_error_mayor_25['TiempodeOrigen'].dt.year).size()

    print(conteo_sismos)

def mostrar_sismo_menor_cantidad_fases():
    print(df.nsmallest(1, 'NF'))

def iniciosesion(usuario):
    nombre = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")

    with open('usuarios.csv', 'r') as archivo:
        for line in archivo:
            item = line.split(',')
            if nombre in item[0] and contrasena in item[1]:
                print("Inicio de sesión exitoso")
                return
    print("Usuario o contraseña incorrectos")
    

def crearusuario(usuario):
    nombre = input("Ingrese el nombre de usuario: ")

    # Verificar si el nombre de usuario ya existe
    with open('usuarios.csv', 'r') as archivo:
        usuarios = archivo.readlines()
        for usuario in usuarios:
            if nombre == usuario.split(',')[0]:
                print("El nombre de usuario ya existe. Por favor, elija otro.")
                return

    contrasena = input("Ingrese la contraseña: ")

    # Crear el nuevo usuario
    with open('usuarios.csv', 'a') as archivo:
        informacion = nombre + ',' + contrasena + '\n'
        archivo.write(informacion)

    
    print("Usuario creado exitosamente")


def crearnotas(usuario):

    # Initialize 'notas' column as an object column if it doesn't exist
    if 'notas' not in usuario.columns:
        usuario['notas'] = pd.Series([], dtype=object)

    # Editar notas
    usuario_input = input("Ingrese el usuario: ")
    # Check if the user exists
    if usuario_input not in usuario['nombre'].values:
        print("Usuario no encontrado")
        return usuario

    # Find the index of the user's row
    usuario_index = usuario[usuario['nombre'] == usuario_input].index[0]

    # Check if the user has notes
    if pd.isna(usuario.loc[usuario_index, 'notas']):
        # If the user doesn't have notes, create a new list with the note
        usuario.at[usuario_index, 'notas'] = [input("Ingrese la nueva nota: ")]
    else:
        # If the user already has notes, append the new note to the list
        notas = usuario.at[usuario_index, 'notas']
    # If notas is a string, convert it to a list
        if isinstance(notas, str):
            notas = [notas]
        notas.append(input("Ingrese la nueva nota: "))
        usuario.at[usuario_index, 'notas'] = notas

def verperfil():
    # Ask for the username
    usuario_input = input("Ingrese el usuario: ")

    # Check if the user exists
    if usuario_input not in usuario['nombre'].values:
        print("Usuario no encontrado")
        return

    # Find the user's row
    usuario_row = usuario[usuario['nombre'] == usuario_input]

    # Print the user's profile
    print(usuario_row)

def editarnotas(usuario):

    # Editar notas
    usuario_input = input("Ingrese el usuario: ")
    # Check if the user exists
    if usuario_input not in usuario['nombre'].values:
        print("Usuario no encontrado")
        return usuario

    # Find the index of the user's row
    usuario_index = usuario[usuario['nombre'] == usuario_input].index[0]

    # Check if the user has notes
    if pd.isna(usuario.loc[usuario_index, 'notas']) or not usuario.loc[usuario_index, 'notas']:
        print("El usuario no tiene notas")
        return usuario

    # Enumerate and print the notes
    for i, nota in enumerate(usuario.loc[usuario_index, 'notas']):
        print(f"{i+1}: {nota}")

    # Ask the user which note they want to edit
    nota_index = int(input("Ingrese el número de la nota que quiere editar: ")) - 1

    # Check if the index is valid
    if nota_index < 0 or nota_index >= len(usuario.loc[usuario_index, 'notas']):
        print("Número de nota inválido")
        return usuario
    nueva_nota = input("Ingrese la nueva nota: ")

    # Replace the old note with the new note
    usuario.at[usuario_index, 'notas'][nota_index] = nueva_nota

    print("Nota editada exitosamente")
    return usuario




def eliminarnotas(usuario):
    # Preguntar al usuario cuál nota quiere eliminar
    usuario_input = input("Ingrese el usuario: ")

    # verificar si el usuario existe
    if usuario_input not in usuario['nombre'].values:
        print("Usuario no encontrado")
        return usuario

    # encontrar el índice de la fila del usuario
    usuario_index = usuario[usuario['nombre'] == usuario_input].index[0]

    # Verificar si el usuario tiene notas
    if pd.isna(usuario.loc[usuario_index, 'notas']):
        print("El usuario no tiene notas")
        return usuario

    # Imprimir las notas del usuario con índices
    for i, nota in enumerate(usuario.loc[usuario_index, 'notas']):
        print(f"{i}: {nota}")

    indice_nota = int(input("Ingrese el índice de la nota que quiere eliminar: "))

    # Eliminar la nota
    del usuario.at[usuario_index, 'notas'][indice_nota]
    return usuario

def cerrarsesion():
    guardar_datos(usuario)
    print("Cerrando sesión")


def sismos_sensibles():
    # Filtrar los sismos sensibles
    sismos_sensibles = df[df['Sensible'] == 'si']

    # Contar cuántos sismos sensibles han ocurrido en promedio por día del mes
    conteo_sismos = sismos_sensibles.groupby(sismos_sensibles['TiempodeOrigen'].dt.day).size()

    print(conteo_sismos)
    print("Promedio de sismos sensibles por día del mes: ", conteo_sismos.mean())

def mapageopandas():
    import geopandas as gpd


def guardar_datos(usuario):
    # Guardar los datos en el archivo CSV existente
    usuario.to_csv('usuarios.csv', mode='a', header=False, index=False)

    print("Datos guardados exitosamente")

# menu con registro de usuarios
while opcion != 17:
    print("-------------------Menú de opciones------------------------------------")
    print("1. Mostrar al usuario la cantidad de sismos que han ocurrido en los últimos 5 años y los nombres de las variables que comprenden el conjunto de datos")
    print("2. Sismos ocurridos en año seleccionado")
    print("3. Primeros 10 sismos en territorio nacional año seleccionado")
    print("4. Mostrar los n primeros sismos de menor intensidad. El n lo debe ingresar el usuario")
    print("5. Mostrar los 10 sismos que fueron detectados por el menor número de estaciones en el año n. El n lo ingresa el usuario")
    print("6. Mostrar cual ha sido la magnitud promedio de los sismos en un año x, que ingrese el usuario.")
    print("7. Mostrar el promedio de la magnitud y profundidad de los sismos por mes. ¿En qué meses se producen los sismos de menor intensidad? Debe dar la opción de ver la información gráficamente, el usuario debe seleccionar si quiere ver la gráfica de magnitud o de profundidad.")
    print("8. Mostrar cuantos sismos sensibles han ocurrido en promedio por año. El sistema debe dar la opción de visualizar una gráfica.")
    print("9. Mostrar cuantos sismos por año tienen un error mayor a 25kms en su localización")
    print("10. Mostrar toda la información del sismo que ha tenido la menor cantidad de fases hasta el momento.")
    print("11. Crear usuarios")
    print("12. Iniciar sesión")
    print("13. Ver perfil")
    print("14. Crear, editar o borrar notas")
    print("15. Sismos sensibles")
    print("16. Mapa geopandas guatemala")
    print("17. Cerrar sesión")
    print("11. Salir")
    
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        #mostrar cantidad de sismos en los ultimos 5 años y nombres de las variables
        anos5()
    elif opcion == 2:
        #sismos ocurridos en un año seleccionado
        anio = int(input("Ingrese el año: "))
        mostrar_sismos_anio(anio)
    elif opcion == 3:
        #primeros 10 sismos en territorio nacional año seleccionado
        anio = int(input("Ingrese el año: "))
        mostrar_primeros_10_territorio_nacional(anio)
    elif opcion == 4:
        #mostrar los n primeros sismos de menor intensidad
        n = int(input("Ingrese el valor de n: "))
        mostrar_n_primeros_menor_intensidad(n)
    elif opcion == 5:
        #mostrar los 10 sismos que fueron detectados por el menor número de estaciones en el año n
        anio = int(input("Ingrese el año: "))
        mostrar_10_sismos_menor_estaciones(anio)
    elif opcion == 6:
        #mostrar cual ha sido la magnitud promedio de los sismos en un año x
        anio = int(input("Ingrese el año: "))
        promediomagnitud(anio)
    elif opcion == 7:
        #mostrar el promedio de la magnitud y profundidad de los sismos por mes
        mes = int(input("Ingrese el mes: "))
        mostrar_promedio_magnitud(mes)
    elif opcion == 8:
        #mostrar cuantos sismos sensibles han ocurrido en promedio por año
        mostrar_sismos_sensibles()
    elif opcion == 9:
        #mostrar cuantos sismos por año tienen un error mayor a 25kms en su localización
        mostrar_sismos_error_localizacion()
    elif opcion == 10:
        #mostrar toda la informacion del sismo que ha tenido la menor cantidad de fases hasta el momento
        mostrar_sismo_menor_cantidad_fases()
    elif opcion == 11:
        #crear usuarios
        crearusuario(usuario)
        guardar_datos(usuario)
    elif opcion == 12:
        #iniciar sesion
        iniciosesion(usuario)
    elif opcion == 13:
        #ver perfil
        verperfil()
    elif opcion == 14:
        #crear, editar o borrar notas
        opcion = int(input("1. Crear notas\n2. Editar notas\n3. Eliminar notas\nIngrese una opción: "))
        if opcion == 1:
            crearnotas(usuario)
            guardar_datos(usuario)
        elif opcion == 2:
            editarnotas(usuario)
        elif opcion == 3:
            eliminarnotas(usuario)
    elif opcion == 15:
        #sismos sensibles
        sismos_sensibles()
guardar_datos(usuario)
print("Fin del programa")
        


