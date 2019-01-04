import pandas as pd

def menu():
    opcion = -1
    while (opcion < 0 or opcion > 1):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Confeccionar producto\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        producir()

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

def reducirMaterias(materias, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv')
    for materia in materias:
        df.loc[df['Materia prima'] == materia, 'Cantidad'] = df.loc[df['Materia prima'] == materia, 'Cantidad'] - cantidad
    df.to_csv('csv/stock_productos.csv', index=False)

def aumentarProducto(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv')
    df.loc[df['Producto'] == producto, 'Cantidad'] = df.loc[df['Producto'] == producto, 'Cantidad'] + cantidad
    df.to_csv('csv/stock_productos.csv', index=False)

def stockFaltante(materia, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv')
    filaMateria = df[df['Materia prima'] == materia]
    stock = filaMateria['Cantidad'].values[0]
    faltante = cantidad - stock
    return faltante

def comprobarStock(materias, cantidad):
    faltantes = []
    for materia in materias:
        faltante = stockFaltante(materia, cantidad)
        if (faltante > 0):
            faltantes.append((materia, faltante))
        
    return faltantes


def cargarTxt():
    productos = []
    archivo = open('confeccion.txt', 'r')
    contenido = archivo.readlines()
    archivo.close()

    for linea in contenido:
        lineaLimpia = linea.strip()
        productos.append(lineaLimpia.split(','))
    
    return productos


producir()