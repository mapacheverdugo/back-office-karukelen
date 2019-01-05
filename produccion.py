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
    opcion = -1
    while (opcion < 0 or opcion > 1):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Confeccionar producto\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        producir()
        menu()

# Función que se encarga de confeccionar un producto (Opción 1 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def producir():
    opcion = -1
    productos = cargarTxt()

    while (opcion < 0 or opcion > len(productos)):
        for index, producto in enumerate(productos):
            print(str(index + 1) + '.', producto[0])
        print('0. Cancelar')
    
        opcion = eval(input('Ingrese el producto a confeccionar: ')) - 1
    
    producto = productos[opcion][0]
    materiasPrima = productos[opcion][1:]
    cantidad = eval(input('Ingrese la cantidad de ' + producto + ' que quiere producir: '))
    materiasFaltantes = comprobarStock(materiasPrima, cantidad)
    if (len(materiasFaltantes) == 0):
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
    df = pd.read_csv('csv/stock_materia_prima.csv')
    for materia in materias:
        df.loc[df['Materia prima'] == materia, 'Cantidad'] = df.loc[df['Materia prima'] == materia, 'Cantidad'] - cantidad
    df.to_csv('csv/stock_productos.csv', index=False)

# Función que aumenta el stock de un producto
# Entrada:  [producto] corresponde al producto que se aumentará
#           [cantidad] correponde a la cantidad que se aumentará el producto
# Salida: Sin valores de retorno
def aumentarProducto(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv')
    df.loc[df['Producto'] == producto, 'Cantidad'] = df.loc[df['Producto'] == producto, 'Cantidad'] + cantidad
    df.to_csv('csv/stock_productos.csv', index=False)

# Función que devuelve el stock faltante de una materia prima
# Entrada:  [materia] corresponde a la materia prima a la que se le debe calcular el stock faltante
#           [cantidad] correponde a la cantidad de materia prima necesaria
# Salida: Devuelve un valor númerico correspondiende al stock faltante, puede ser positivo (falta), negativo (sobra) o 0
def stockFaltante(materia, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv')
    filaMateria = df[df['Materia prima'] == materia]
    stock = filaMateria['Cantidad'].values[0]
    faltante = cantidad - stock
    return faltante

# Función que comprueba el stock de todas las materias primas ingresadas
# Entrada:  [materias] corresponde a una lista de materias primas a revisar
#           [cantidad] correponde a la cantidad de materias prima necesaria
# Salida: Devuelve una lista de tuplas de todas las materias primas faltantes, junto con la cantidad que falta
def comprobarStock(materias, cantidad):
    faltantes = []
    for materia in materias:
        faltante = stockFaltante(materia, cantidad)
        if (faltante > 0):
            faltantes.append((materia, faltante))
        
    return faltantes

# Función que se encarga de procesar el archivo TXT de las confecciones de materia prima
# Entrada: Sin parámetros de entrada 
# Salida: Lista de listas que contiene cada producto en la primera posición ([0]) y sus materias prima necesarias para confeccionarlo
def cargarTxt():
    productos = []
    archivo = open('confeccion.txt', 'r')
    contenido = archivo.readlines()
    archivo.close()

    for linea in contenido:
        lineaLimpia = linea.strip()
        productos.append(lineaLimpia.split(','))
    
    return productos