# IMPORTACIÓN_DE_FUNCIONES

import pandas as pd

def menu():
    opcion = -1
    while (opcion < 0 or opcion > 4):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Ver pedidos\n")
        print("2. Procesar pedido\n")
        print("3. Mostrar a el/los pedido(s) de mayor utilidad\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        mostrarPedidos()
    elif (opcion == 2):
        print("Calcular capital seleccionado")
    elif (opcion == 3):
        print(obtenerMayorPedido)

def mostrarPedidos():
    df = pd.read_csv('pedidos.csv')
    print(df)
    
def procesarPedido(numeroPedido):
    df = pd.read_csv('csv/pedidos.csv')
    pedido = df.loc[numeroPedido]
    hayStockDeTodos = True
    for producto, cantidad in pedido.iteritems():
        if (producto != 'Cliente'): # Se descarta el primer elemento porque corresponde al nombre del cliente
            if (hayStock(producto, cantidad) == False):
                print('No hay stock suficiente de', producto)
                hayStockDeTodos = False

    if (hayStockDeTodos):
        for producto, cantidad in pedido.iteritems():
            if (producto != 'Cliente'): # Se descarta el primer elemento porque corresponde al nombre del cliente
                reducirStock(producto, cantidad)
                eliminarPedido(producto)
    else:
        print('No se pudo procesar el pedido', numeroPedido)


def hayStock(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv')
    filaProducto = df[df['Producto'] == producto]
    stock = filaProducto['Cantidad'].values

    if (stock >= cantidad):
        return True
    else:
        return False

def reducirStock(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv')
    df.loc[df['Producto'] == producto, 'Cantidad'] = df.loc[df['Producto'] == producto, 'Cantidad'] - cantidad
    df.to_csv('csv/stock_productos.csv', index=False)

def eliminarPedido(numeroPedido):
    df = pd.read_csv('csv/pedidos.csv')
    df = df.drop(numeroPedido)
    df.to_csv('csv/pedidos.csv', index=False)

def obtenerMayorPedido():
    indexMayor = 0
    valorMayor = 0
    df = pd.read_csv('csv/pedidos.csv')
    for index, pedido in df.iterrows():
        valorActual = 0
        for producto, cantidad in pedido.iteritems():
            if (producto != 'Cliente'):
                valorActual = valorActual + obtenerPrecio(producto)
        if (valorActual > valorMayor):
            valorMayor = valorActual
            indexMayor = index
    pedido = df.loc[indexMayor]
    return pedido

def obtenerPrecio(producto):
    df = pd.read_csv('csv/precios_productos.csv')
    filaProducto = df[df['Producto'] == producto]
    precio = filaProducto['Precio'].values[0]
    return precio

obtenerMayorPedido()

