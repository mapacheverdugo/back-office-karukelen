import pandas as pd

def menu():
    opcion = 0
    while (opcion < 1 or opcion > 2):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Leer y organizar los archivos\n")
        print("2. Calcular el capital total de la empresa\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        procesarInventario('entrada.txt')
    elif (opcion == 2):
        print("Calcular capital seleccionado")
    else:
        print("Error, no existe la opción seleccionada")

# Función que abre el archivo .txt del inventario de la empresa
# Entrada: El nombre del archivo
# Salida: Una lista de listas que tiene cada sección del archivo separada
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
    
# Función que crea los archivos .csv del inventario
# Entrada: Los datos de la sección en una lista, las cabeceras de cada columna y el nombre del archivo a generar
# Salida: No hay salida de datos
def crearCsv(datos, titulos, nombre):
    directorio = 'csv/' # Carpeta donde se guardarán los archivos .csv
    tabla = []
    for linea in datos:
        celdas = linea.split(' ')
        tabla.append(celdas)

    df = pd.DataFrame(tabla, columns=titulos)
    df.to_csv(directorio + nombre)

# Función encargada de procesar las secciones
# Entrada: La lista de lista generada por cargarTxt()
# Salida: No hay salida de datos
def procesarInventario(nombre):
    i = 0
    datosInventario = cargarTxt(nombre)
    nombre = 'archivo.csv' # Nombre del archivo a crear
    titulos = []
    for seccion in datosInventario:
        if (i == 0):
            nombre = 'ventas_mes.csv'
            titulos = ['Mes', 'Ventas']
        elif (i == 1):
            nombre = 'precios_productos.csv'
            titulos = ['Producto', 'Precio']
        elif (i == 2):
            nombre = 'stock_materia_prima.csv'
            titulos = ['Materia prima', 'Cantidad']
        else:
            nombre = 'stock_productos.csv'
            titulos = ['Producto', 'Cantidad']

        crearCsv(datosInventario[i], titulos, nombre)
        i = i + 1



procesarInventario('entrada.txt')