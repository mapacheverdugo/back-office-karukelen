# Javier Berrios,
# Rodrigo Paredes,
# Tomas Quintana,
# Carlos Sepúlveda,
# Héctor Vásquez.
# Python 3.7 (10 de diciembre, 2018).

# IMPORTACIÓN_DE_FUNCIONES

import pandas as pd

# DEFINICIÓN_DE_FUNCIONES

# Función encargada de ejecutar el menú propio de la producción
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def menu(): 
    opcion = -1  # Se define un valor distinto a 0 y 1
    while (opcion < 0 or opcion > 1): # Si la opción seleccionada es distinta a las opciones disponibles se muestra el menú
        print("\n¿Qué acción desea realizar?\n")
        print("1. Confeccionar producto\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: ")) # Se le pide al usuario que ingrese un valor
    
    if (opcion == 1):
        producir()
        menu() # Cuando termina, se llama al menú para que se ejecute de nuevo

# Función que se encarga de confeccionar un producto (Opción 1 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def producir():
    opcion = -1 # Se define un valor negativo para que entre al while
    productos = cargarTxt() # Se traen los productos

    while (opcion < 0 or opcion > len(productos)): # Mientras la opción seleccionada sea distinto al numero del algún pedido
        for index, producto in enumerate(productos):
            print(str(index + 1) + '.', producto[0]) # Muestra la lista de productos con número
        print('0. Cancelar')
    
        opcion = eval(input('Ingrese el producto a confeccionar: ')) - 1 # Se le pide al usuario que ingrese un valor
    
    producto = productos[opcion][0] # Guarda el producto seleccionado
    materiasPrima = productos[opcion][1:] # Guarda las materias primas necesarias para fabricar ese producto
    cantidad = eval(input('Ingrese la cantidad de ' + producto + ' que quiere producir: ')) # Se le pide al usuario que ingrese la cantidad a producir
    materiasFaltantes = comprobarStock(materiasPrima, cantidad) # Comprueba que materias primas faltan y las guarda
    if (len(materiasFaltantes) == 0): # Si no falta ninguna materia prima
        # Se procesa la solicitud de producción
        reducirMaterias(materiasPrima, cantidad) 
        aumentarProducto(producto, cantidad)
    else:
        print('No se puede producir', producto, 'ya que faltan las siguiente materias primas:')
        for materia, cantidad in materiasFaltantes:
            print(cantidad, 'unidades de', materia)

# Función que reduce el stock de las materias primas
# Entrada:  [materias] corresponde a las materias primas que se reducirán
#           [cantidad] correponde a la cantidad a reducir cada materia prima
# Salida: Sin valores de retorno
def reducirMaterias(materias, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv') # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    for materia in materias:
        df.loc[df['Materia prima'] == materia, 'Cantidad'] = df.loc[df['Materia prima'] == materia, 'Cantidad'] - cantidad # Se le resta la cantidad de materia prima
    df.to_csv('csv/stock_productos.csv', index=False) # Se guardan los cambios en csv/stock_productos.csv

# Función que aumenta el stock de un producto
# Entrada:  [producto] corresponde al producto que se aumentará
#           [cantidad] correponde a la cantidad que se aumentará el producto
# Salida: Sin valores de retorno
def aumentarProducto(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv') # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    df.loc[df['Producto'] == producto, 'Cantidad'] = df.loc[df['Producto'] == producto, 'Cantidad'] + cantidad # Se aumenta el stock del producto en cierta cantidad
    df.to_csv('csv/stock_productos.csv', index=False) # Se guardan los cambios en csv/stock_productos.csv

# Función que devuelve el stock faltante de una materia prima
# Entrada:  [materia] corresponde a la materia prima a la que se le debe calcular el stock faltante
#           [cantidad] correponde a la cantidad de materia prima necesaria
# Salida: Devuelve un valor númerico correspondiende al stock faltante, puede ser positivo (falta), negativo (sobra) o 0
def stockFaltante(materia, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv') # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    filaMateria = df[df['Materia prima'] == materia] # Se busca la materia prima por nombre y se guarda
    stock = filaMateria['Cantidad'].values[0] # Se guarda el stock de esa materia prima
    faltante = cantidad - stock # Se calcula el stock faltante restando lo necesario menos el total
    return faltante

# Función que comprueba el stock de todas las materias primas ingresadas
# Entrada:  [materias] corresponde a una lista de materias primas a revisar
#           [cantidad] correponde a la cantidad de materias prima necesaria
# Salida: Devuelve una lista de tuplas de todas las materias primas faltantes, junto con la cantidad que falta
def comprobarStock(materias, cantidad):
    faltantes = [] # Lista que guaradará todas la materias primas que les falte stock
    for materia in materias:
        faltante = stockFaltante(materia, cantidad)
        if (faltante > 0): # Si falta stock
            faltantes.append((materia, faltante)) # Se agrega esa materia prima y su stock faltante a la lista
        
    return faltantes

# Función que se encarga de procesar el archivo TXT de las confecciones de materia prima
# Entrada: Sin parámetros de entrada 
# Salida: Lista de listas que contiene cada producto en la primera posición ([0]) y sus materias prima necesarias para confeccionarlo
def cargarTxt():
    productos = []
    archivo = open('confeccion.txt', 'r') # Abre el archivo de texto confección.txt
    contenido = archivo.readlines() # Lee el contenido del archivo y lo guarda
    archivo.close() # Cierra el archivo

    for linea in contenido:
        lineaLimpia = linea.strip() # Se limpia la linea de los espaciós y saltos de linea innecesarios
        productos.append(lineaLimpia.split(',')) # Se separa esa linea en cada lugar que haya una coma y se agrega a la lista de productos
    
    return productos