# Javier Berrios,
# Rodrigo Paredes,
# Tomas Quintana,
# Carlos Sepúlveda,
# Héctor Vásquez.
# Python 3.7 (10 de diciembre, 2018).

# IMPORTACIÓN_DE_FUNCIONES

import pandas as pd

# DEFINICIÓN_DE_FUNCIONES

# Función encargada de ejecutar el menú propio del inventario
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def menu():
    opcion = -1
    while (opcion < 0 or opcion > 2):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Leer y organizar los archivos\n")
        print("2. Calcular el capital total de la empresa\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        procesarInventario()
        menu()
    elif (opcion == 2):
        print("Calcular capital seleccionado")
        menu()

# Función que se encarga de procesar y separar el archivo TXT del inventario en secciones
# Entrada: [nombre] correponde al nombre del archivo de texto donde está el inventario
# Salida: Lista de listas que contiene las secciones del inventario separadas línea a línea
def cargarTxt(nombre):
    secciones = []
    seccion = []
    archivo = open(nombre, 'r')
    contenido = archivo.readlines()
    archivo.close()

    for linea in contenido:
        lineaLimpia = linea.strip()
        if (lineaLimpia == '-'):
            secciones.append(seccion)
            seccion = []
        else:
            seccion.append(lineaLimpia)

    return secciones
    
# Función que crea los archivos CSV del inventario
# Entrada:  [datos] corresponde a cada sección del inventario
#           [titulos] corresponde a una lista con los títulos de cada columna
#           [nombre] corresponde al nombre del archivo que se va a crear
# Salida: No hay salida de datos
def crearCsv(datos, titulos, nombre):
    directorio = 'csv/' # Carpeta donde se guardarán los archivos .csv
    tabla = [] # Variable que guardará una lista de listas
    for linea in datos:
        celdas = linea.split(' ') # Se separa la linea en cada lugar que haya un espacio
        tabla.append(celdas) # Se agregan la lista celdas a la lista tablas

    df = pd.DataFrame(tabla, columns=titulos) # Se crea una tabla CSV con la lista de listas
    df.to_csv(directorio + nombre) # Se guarda el archivo CSV con los datos de la lista de lista

# Función que se encarga de procesar todo el inventario (Opción 1 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def procesarInventario():
    i = 0
    nombre = input("Ingrese el nombre del archivo donde esta el inventario: ") # Se guardan los cambios en csv/stock_productos.csv
    datosInventario = cargarTxt(nombre)
    nombre = 'archivo.csv' # Nombre del archivo a crear
    titulos = []
    for i, seccion in enumerate(datosInventario):
        if (i == 0):
            nombre = 'ventas_mes.csv'
            titulos = ['Mes', 'Ventas'] # Encabezados para las columnas de ventas por mes
        elif (i == 1):
            nombre = 'precios_productos.csv'
            titulos = ['Producto', 'Precio'] # Encabezados para las columnas de precios por producto
        elif (i == 2):
            nombre = 'stock_materia_prima.csv'
            titulos = ['Materia prima', 'Cantidad'] # Encabezados para las columnas stock de las materias prima
        else:
            nombre = 'stock_productos.csv'
            titulos = ['Producto', 'Cantidad'] # Encabezados para las columnas del stock de los productos

        crearCsv(datosInventario[i], titulos, nombre)
