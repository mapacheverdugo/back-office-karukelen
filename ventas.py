# Javier Berrios,
# Rodrigo Paredes,
# Tomas Quintana,
# Carlos Sepúlveda,
# Héctor Vásquez.
# Python 3.7 (10 de diciembre, 2018).

# IMPORTACIÓN_DE_FUNCIONES

import pandas as pd

# DEFINICIÓN_DE_FUNCIONES

# Función encargada de ejecutar el menú propio de las ventas
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def menu():
    opcion = -1
    while (opcion < 0 or opcion > 3):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Ver pedidos\n")
        print("2. Procesar pedido\n")
        print("3. Mostrar a el/los pedido(s) de mayor utilidad\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        mostrarPedidos()
        menu()
    elif (opcion == 2):
        procesarPedido()
        menu()
    elif (opcion == 3):
        mostrarMayorPedido()
        menu()

# Función encargada de mostrar todos los pedidos (Opción 1 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def mostrarPedidos():
    df = pd.read_csv('csv/pedidos.csv')
    print(df)

# Función encargada de procesar un pedido (Opción 2 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def procesarPedido():
    df = pd.read_csv('csv/pedidos.csv')
    mostrarPedidos()
    numeroPedido = eval(input("Ingrese el número del pedido que quiere procesar: "))
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

# Función que dice si hay stock de un producto
# Entrada:  [producto] corresponde al producto a comprobar si tiene stock disponible
#           [cantidad] correponde a la cantidad que debe haber de producto
# Salida: Devuelve True cuando hay stock del producto y False cuando no
def hayStock(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv')
    filaProducto = df[df['Producto'] == producto]
    stock = filaProducto['Cantidad'].values

    if (stock >= cantidad):
        return True
    else:
        return False

# Función que disminuye el stock de un producto
# Entrada:  [producto] corresponde al producto que se reducirá
#           [cantidad] correponde a la cantidad a reducir del producto
# Salida: Sin valores de retorno
def reducirStock(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv')
    df.loc[df['Producto'] == producto, 'Cantidad'] = df.loc[df['Producto'] == producto, 'Cantidad'] - cantidad
    df.to_csv('csv/stock_productos.csv', index=False)

# Función que elimina un pedido del archivo de pedidos
# Entrada: [numeroPedido] corresponde al numero de fila del pedido a eliminar
# Salida: Sin valores de retorno
def eliminarPedido(numeroPedido):
    df = pd.read_csv('csv/pedidos.csv')
    df = df.drop(numeroPedido)
    df.to_csv('csv/pedidos.csv', index=False)

# Función encargada de mostar el pedido que genera mayor utilidad (Opción 3 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def mostrarMayorPedido():
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
    print(pedido)

# Función que entrega el precio de un producto
# Entrada: [producto] corresponde al producto a comprobar su precio
# Salida: Devuelve el precio del producto
def obtenerPrecio(producto):
    df = pd.read_csv('csv/precios_productos.csv')
    filaProducto = df[df['Producto'] == producto]
    precio = filaProducto['Precio'].values[0]
    return precio

