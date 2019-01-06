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
    opcion = -1 # Se define un valor distinto a 0, 1, 2 y 3
    while (opcion < 0 or opcion > 3): # Si la opción seleccionada es distinta a las opciones disponibles se muestra el menú
        print("\n¿Qué acción desea realizar?\n")
        print("1. Ver pedidos\n")
        print("2. Procesar pedido\n")
        print("3. Mostrar a el/los pedido(s) de mayor utilidad\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: ")) # Se le pide al usuario que ingrese un valor
    
    if (opcion == 1):
        mostrarPedidos()
        menu() # Cuando termina, se llama al menú para que se ejecute de nuevo
    elif (opcion == 2):
        procesarPedido()
        menu() # Cuando termina, se llama al menú para que se ejecute de nuevo
    elif (opcion == 3):
        mostrarMayorPedido()
        menu() # Cuando termina, se llama al menú para que se ejecute de nuevo

# Función encargada de mostrar todos los pedidos (Opción 1 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def mostrarPedidos():
    df = pd.read_csv('csv/pedidos.csv') # Abre el archivo csv/pedidos.csv y lo guarda en forma de tabla
    print(df) 

# Función encargada de procesar un pedido (Opción 2 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def procesarPedido():
    df = pd.read_csv('csv/pedidos.csv') # Abre el archivo csv/pedidos.csv y lo guarda en forma de tabla
    mostrarPedidos()
    numeroPedido = eval(input("Ingrese el número del pedido que quiere procesar: ")) # Se le pide al usuario que ingrese el número de pedido
    pedido = df.loc[numeroPedido] # Obtiene el pedido que esté en la fila con el numero ingresado
    hayStockDeTodos = True # Variable para revisar si todos los productos del pedido tienen stock
    for producto, cantidad in pedido.iteritems():
        if (producto != 'Cliente'): # Se descarta el primer elemento porque corresponde al nombre del cliente
            if (hayStock(producto, cantidad) == False): # Si no hay stock de alguno
                print('No hay stock suficiente de', producto)
                hayStockDeTodos = False # Se cambia la variable de que no hay stock

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
    df = pd.read_csv('csv/stock_productos.csv') # Abre el archivo csv/stock_productos.csv y lo guarda en forma de tabla
    filaProducto = df[df['Producto'] == producto] # Busca el producto por el nombre en la tabla
    stock = filaProducto['Cantidad'].values # Guarda el stock del producto

    if (stock >= cantidad):
        return True
    else:
        return False

# Función que disminuye el stock de un producto
# Entrada:  [producto] corresponde al producto que se reducirá
#           [cantidad] correponde a la cantidad a reducir del producto
# Salida: Sin valores de retorno
def reducirStock(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv') # Abre el archivo csv/stock_productos.csv y lo guarda en forma de tabla
    df.loc[df['Producto'] == producto, 'Cantidad'] = df.loc[df['Producto'] == producto, 'Cantidad'] - cantidad # Busca el producto por el nombre, y se le resta la cantidad
    df.to_csv('csv/stock_productos.csv', index=False) # Se guardan los cambios en csv/stock_productos.csv

# Función que elimina un pedido del archivo de pedidos
# Entrada: [numeroPedido] corresponde al numero de fila del pedido a eliminar
# Salida: Sin valores de retorno
def eliminarPedido(numeroPedido):
    df = pd.read_csv('csv/pedidos.csv') # Abre el archivo csv/pedidos.csv y lo guarda en forma de tabla
    df = df.drop(numeroPedido) # Se elimina la fila que tiene el número ingresado
    df.to_csv('csv/pedidos.csv', index=False) # Se guardan los cambios en csv/stock_productos.csv

# Función encargada de mostar el pedido que genera mayor utilidad (Opción 3 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def mostrarMayorPedido():
    indexMayor = 0 # Variable donde se guardará el índice del pedido mayor
    valorMayor = 0 # Variable donde se guardará el valor del pedido mayor
    df = pd.read_csv('csv/pedidos.csv') # Abre el archivo csv/pedidos.csv y lo guarda en forma de tabla
    for index, pedido in df.iterrows():
        valorActual = 0
        for producto, cantidad in pedido.iteritems():
            if (producto != 'Cliente'): # Se descarta la fila del cliente, ya que solo nos interesan los productos
                valorActual = valorActual + obtenerPrecio(producto) # Al velor del pedido actual se suma el precio del producto
        if (valorActual > valorMayor): # Si el valor atual es mayor que el valor guardado
            valorMayor = valorActual # El valor actual pasa a ser el mayor
            indexMayor = index # El inidce actual pasa a ser el indice del valor mayor
    pedido = df.loc[indexMayor] # Se busca la fila que tiene el numero del valor mayor
    print(pedido)

# Función que entrega el precio de un producto
# Entrada: [producto] corresponde al producto a comprobar su precio
# Salida: Devuelve el precio del producto
def obtenerPrecio(producto):
    df = pd.read_csv('csv/precios_productos.csv') # Abre el archivo csv/pedidos.csv y lo guarda en forma de tabla
    filaProducto = df[df['Producto'] == producto] # Busca el producto por el nombre
    precio = filaProducto['Precio'].values[0] # Guarda el precio del producto
    return precio

