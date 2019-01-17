# Back office es el apoyo empresarial de servicios financieros. 
# Se llevan a cabo funciones de gestión como, por ejemplo: 
# el mantenimiento de registros, contabilidad, organización, 
# control de recursos, entre otros. 
# En el siguiente programa se quiere conseguir un control 
# de los recursos empleados por la empresa Karükelen ya que 
# la empresa aumentó su demanda en un 200%, debido a esto necesita 
# optimizar sus recursos, eligiendo ciertos proveedores y vendiendo 
# a ciertos clientes que le otorguen la mayor utilidad financiera.

# Javier Berrios,
# Rodrigo Paredes,
# Tomas Quintana,
# Carlos Sepúlveda,
# Héctor Vásquez.
# Python 3.7 (10 de diciembre, 2018).

# IMPORTACIÓN_DE_FUNCIONES

import pandas as pd

# DEFINICIÓN_DE_FUNCIONES

# Función encargada de ejecutar el menú principal
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def menuPrincipal():
    opcion = 0
    while (opcion < 1 or opcion > 4):
        print("MENÚ\n\n")
        print("Seleccione un submenú\n")
        print("1. Inventario\n")
        print("2. Poducción\n")
        print("3. Ventas\n")
        print("4. Compras\n\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        menuInventario()
    elif (opcion == 2):
        menuProduccion()
    elif (opcion == 3):
        menuVentas()
    elif (opcion == 4):
        menuCompras()
    else:
        print("Error, no existe la opción seleccionada")

# Función encargada de ejecutar el menú propio del inventario
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def menuInventario():
    opcion = -1
    while (opcion < 0 or opcion > 2):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Leer y organizar los archivos\n")
        print("2. Calcular el capital total de la empresa\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        procesarInventario()
        menuInventario()
    elif (opcion == 2):
        mostrarCapital()
        menuInventario()

# Función encargada de ejecutar el menú propio de las ventas
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def menuVentas():
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
        menuVentas() # Cuando termina, se llama al menú para que se ejecute de nuevo
    elif (opcion == 2):
        procesarPedido()
        menuVentas() # Cuando termina, se llama al menú para que se ejecute de nuevo
    elif (opcion == 3):
        mostrarMayorPedido()
        menuVentas() # Cuando termina, se llama al menú para que se ejecute de nuevo

def menuCompras():
    opcion = -1
    while (opcion < 0 or opcion > 3):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Ver materias disponibles para comprar\n")
        print("2. Ver proveedor más conveniente\n")
        print("3. Comprar materia prima más conveniente\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        mostrarListaEnumerada(listaDeMateriasSinRepetir())
        menuCompras()
    elif (opcion == 2):
        cotizarMateria()
        menuCompras()
    elif (opcion == 3):
        comprarMateriaPrima()
        menuCompras()

# Función encargada de ejecutar el menú propio de la producción
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def menuProduccion(): 
    opcion = -1  # Se define un valor distinto a 0 y 1
    while (opcion < 0 or opcion > 1): # Si la opción seleccionada es distinta a las opciones disponibles se muestra el menú
        print("\n¿Qué acción desea realizar?\n")
        print("1. Confeccionar producto\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: ")) # Se le pide al usuario que ingrese un valor
    
    if (opcion == 1):
        producir()
        menuProduccion() # Cuando termina, se llama al menú para que se ejecute de nuevo

# Función que se encarga de procesar un archivo TXT y devolver sus lineas como un elemento individual
# Entrada: [nombre] correponde al nombre del archivo TXT a procesar
# Salida: Lista que contiene las lineas del archivo separadas en un elemento individual
def cargarTxt(nombre):
    if (nombre.endswith(".txt") == False): # Si el nombre ingresado NO termina en ".txt"
        nombre = nombre + ".txt" # Se le agrega ese ".txt"
    
    listaLineas = []
    archivo = open(nombre, 'r') # Abre el archivo de texto confección.txt
    contenido = archivo.readlines() # Lee el contenido del archivo y lo guarda
    archivo.close() # Cierra el archivo

    for linea in contenido:
        lineaLimpia = linea.strip() # Se limpia la linea de los espaciós y saltos de linea innecesarios
        listaLineas.append(lineaLimpia)
    return listaLineas

def separarListaLineas(lista, separador):
    listaNueva = []
    for linea in lista:
        lineaSeparada = linea.split(separador)
        listaNueva.append(lineaSeparada)
    return listaNueva

def mostrarListaEnumerada(lista):
    for index, elemento in enumerate(lista):
        print(str(index + 1) + '. ' + elemento)

# Función que crea los archivos CSV del inventario
# Entrada:  [listaDeListas] corresponde a los datos que tendrá el documento .csv
#           [titulos] corresponde a una lista con los títulos de cada columna
#           [nombre] corresponde al nombre del archivo que se va a crear
# Salida: No hay salida de datos
def listaDeListasACsv(listaDeListas, titulos, nombre):
    directorio = 'csv/' # Carpeta donde se guardarán los archivos .csv
    df = pd.DataFrame(listaDeListas, columns=titulos) # Se crea una tabla CSV con la lista de listas
    df.to_csv(directorio + nombre) # Se guarda el archivo CSV con los datos de la lista de lista

# ----- MODULO INVENTARIO -----

def separarSeccionInventario(listaDeLineas):
    secciones = []
    seccion = []
    for linea in listaDeLineas:
        if (linea == '-'):
            secciones.append(seccion)
            seccion = []
        else:
            seccion.append(linea)
    return secciones

# Función que se encarga de procesar todo el inventario (Opción 1 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def procesarInventario():
    i = 0
    nombre = input("Ingrese el nombre del archivo donde esta el inventario: ") # Se guardan los cambios en csv/stock_productos.csv
    listaLineas = cargarTxt(nombre)
    datosInventario = separarSeccionInventario(listaLineas)
    nombre = '' # Nombre del archivo a crear
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

        datosEnTabla = separarListaLineas(seccion, ' ')
        listaDeListasACsv(datosEnTabla, titulos, nombre)


def mostrarCapital():
    capital = capitalEmpresa()
    print("El capital total de la empresa es de " + str(capital))

def capitalEmpresa():
    df = pd.read_csv('csv/ventas_mes.csv')
    capitalAcumulado = 0
    for index, mes in df.iterrows():
        capitalAcumulado = capitalAcumulado + mes['Ventas']
    return capitalAcumulado

# ----- MODULO DE PRODUCCIÓN ------

# Función que se encarga de confeccionar un producto (Opción 1 del menú)
# Entrada: Sin parámetros de entrada 
# Salida: Sin valores de retorno
def producir():
    opcion = -1 # Se define un valor negativo para que entre al while
    listaLineas = cargarTxt('confeccion.txt') # Se traen los productos
    productos = separarListaLineas(listaLineas, ',')

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

# Función que comprueba el stock de todas las materias primas ingresadas
# Entrada:  [materias] corresponde a una lista de materias primas a revisar
#           [cantidad] correponde a la cantidad de materias prima necesaria
# Salida: Devuelve una lista de tuplas de todas las materias primas faltantes, junto con la cantidad que falta
def comprobarStock(materias, cantidad):
    faltantes = [] # Lista que guaradará todas la materias primas que les falte stock
    for materia in materias:
        faltante = stockFaltanteMateria(materia, cantidad)
        if (faltante > 0): # Si falta stock
            faltantes.append((materia, faltante)) # Se agrega esa materia prima y su stock faltante a la lista
        
    return faltantes



# ----- MÓDULO DE VENTAS -----

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
                precio = obtenerPrecio(producto)
                reducirProducto(producto, cantidad)
                aumentarCapital(cantidad * precio)
        eliminarPedido(numeroPedido)
    else:
        print('No se pudo procesar el pedido', numeroPedido)

# Función que dice si hay stock de un producto
# Entrada:  [producto] corresponde al producto a comprobar si tiene stock disponible
#           [cantidad] correponde a la cantidad que debe haber de producto
# Salida: Devuelve True cuando hay stock del producto y False cuando no
def hayStock(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv') # Abre el archivo csv/stock_productos.csv y lo guarda en forma de tabla
    filaProducto = df[df['Producto'] == producto] # Busca el producto por el nombre en la tabla
    stock = filaProducto['Cantidad'].values[0] # Guarda el stock del producto

    if (stock >= cantidad):
        return True
    else:
        return False

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
                valorActual = valorActual + (cantidad * obtenerPrecio(producto)) # Al velor del pedido actual se suma el precio del producto
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


# ----- MODULO DE COMPRAS -----

def listaDeMateriasSinRepetir():
    listaSinRepetir = []
    materiasPrimas = listaDeMaterias()
    for i, proveedor in enumerate(materiasPrimas):
        for tupla in proveedor:
            nombre = tupla[0]
            if (nombre not in listaSinRepetir):
                listaSinRepetir.append(nombre)
    
    return listaSinRepetir

def cotizarMateria():
    opcion = -1 # Se define un valor negativo para que entre al while
    materiasSinRepetir = listaDeMateriasSinRepetir()
    while (opcion < 0 or opcion > len(materiasSinRepetir)):
        mostrarListaEnumerada(materiasSinRepetir)
        print('0. Cancelar')
        opcion = eval(input("Ingrese la materia que desea cotizar: ")) # Se le pide al usuario que ingrese la materia prima
    
    if (opcion != 0):
        materiaACotizar = materiasSinRepetir[opcion - 1]
        proveedor = proveedorMasConveniente(materiaACotizar)

        nombreProveedor = proveedor[1]
        precioPorUnidad = proveedor[2]
        unidadesEnPromocion = str(proveedor[3])
        precioPromocion = str(float(precioPorUnidad) * int(unidadesEnPromocion))

        print("El proveedor " + nombreProveedor + " vende a $" + precioPromocion + " las " + unidadesEnPromocion + " unidades de " + materiaACotizar + ", siendo esta la opción más conveniente")

def obtenerProveedor(indice):
    df = pd.read_csv('csv/proveedores.csv', header=None) # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    return df.loc[indice, 0]

def listaDeMaterias():
    df = pd.read_csv('csv/proveedores.csv', header=None) # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    proveedores = []
    for i, proveedor in df.iterrows():
        precio = proveedor.tail(1).values[0]
        materias = []
        for celda in proveedor.iteritems():
            index = celda[0]
            valor = celda[1]
            if (index != 0 and index != len(proveedor) - 1): # Cuando sea distinto de la primera y última celda significa que será una materia prima
                nombreYCantidad = valor.split(':')
                nombreYCantidad.append(precio)
                materia = tuple(nombreYCantidad)
                
                materias.append(materia)
        proveedores.append(materias)
    return proveedores
                

def proveedorMasConveniente(materia):
    precioMenorUnidad = -1 # Se define un precio incial negativo
    indiceProveedor = -1 # Se define un indice incial negativo
    nombreProveedor = '' # Se define un nombre vacío
    unidadMenor = -1 # Se definen las unidades inciales como negativas

    materiasPrimas = listaDeMaterias() # Se obtienen los datos de todas las materias primas ofrecidas
    for i, proveedor in enumerate(materiasPrimas): 
        for tupla in proveedor:
            nombre = tupla[0] # Se guarda el nombre de la materia prima actual
            unidades = eval(tupla[1]) # Se guardan las unidades en promoción de la materia prima actual
            precio = tupla[2] # Se guarda el precio de la materia prima actual
            if (nombre == materia): # Si el nombre es el mismo que la materia que busco
                precioPorUnidad = precio / unidades # Se guarda el precio por unidad
                if (precioMenorUnidad == -1 or precioMenorUnidad > precioPorUnidad):
                    precioMenorUnidad = precioPorUnidad 
                    indiceProveedor = i
                    nombreProveedor = obtenerProveedor(i)
                    unidadMenor = unidades
    return (indiceProveedor, nombreProveedor, precioMenorUnidad, unidadMenor)

def comprarMateriaPrima():
    opcion = -1 # Se define un valor negativo para que entre al while
    materiasSinRepetir = listaDeMateriasSinRepetir()
    while (opcion < 0 or opcion > len(materiasSinRepetir)):
        mostrarListaEnumerada(materiasSinRepetir)
        print('0. Cancelar')
        opcion = eval(input("Ingrese la materia que desea cotizar: ")) # Se le pide al usuario que ingrese la materia prima

    if (opcion != 0):
        cantidad = eval(input("Ingrese cuantas promociones desea comprar: ")) # Se le pide al usuario que ingrese la cantidad de promociones que desea comprar

        materiaAComprar = materiasSinRepetir[opcion - 1]
        proveedor = proveedorMasConveniente(materiaAComprar) # Guarda los datos del proveedor más conveniente que ofrece esa materia prima
        unidadesEnPromocion = proveedor[3] # Guarda la cantidad de unidades que el proveedor ofrece como parte de la promoción
        precioMateria = proveedor[2]

        if (comprobarCapital(precioMateria * unidadesEnPromocion * cantidad)):
            aumentarMateria(materiaAComprar, unidadesEnPromocion * cantidad) # Aumenta la materia prima
            reducirCapital(precioMateria * unidadesEnPromocion * cantidad)
            print("Se compraron exitosamente " + str(cantidad * unidadesEnPromocion) + " unidades de " + materiaAComprar)
        else:
            print("No hay capital suficiente para realizar esta operación")

# Función que aumenta el monto de las ventas del último mes
# Entrada: [valor] corresponde al monto en que se aumentará el capital del último mes
# Salida: Sin valores de retorno
def aumentarCapital(valor):
    df = pd.read_csv('csv/ventas_mes.csv') # Abre el archivo csv/ventas_mes.csv y lo guarda en forma de tabla
    montoUltimoMes = df.tail(1)['Ventas'].values[0] # Obtiene el monto de ventas del último mes 
    df.iloc[-1, df.columns.get_loc('Ventas')] = montoUltimoMes + valor # Obtiene el último mes (-1) y modifica la columna 'Ventas'
    df.to_csv('csv/ventas_mes.csv', index=False) # Se guardan los cambios en csv/ventas_mes.csv
    

# Función que reduce el monto de las ventas del último mes
# Entrada: [valor] corresponde al monto en que se disminuirá el capital del último mes
# Salida: Sin valores de retorno
def reducirCapital(valor):
    df = pd.read_csv('csv/ventas_mes.csv') # Abre el archivo csv/ventas_mes.csv y lo guarda en forma de tabla
    montoUltimoMes = df.tail(1)['Ventas'].values[0] # Obtiene el monto de ventas del último mes 
    df.iloc[-1, df.columns.get_loc('Ventas')] = montoUltimoMes - valor # Obtiene el último mes (-1) y modifica la columna 'Ventas'
    df.to_csv('csv/ventas_mes.csv', index=False) # Se guardan los cambios en csv/ventas_mes.csv

# Función que comprueba que exista capital suficiente
# Entrada: [monto] corresponde al monto que debe comprobarse que exista
# Salida: Sin valores de retorno
def comprobarCapital(monto):
    df = pd.read_csv('csv/ventas_mes.csv') # Abre el archivo csv/ventas_mes.csv y lo guarda en forma de tabla
    montoUltimoMes = df.tail(1)['Ventas'].values[0] # Obtiene el monto de ventas del último mes 
    if (montoUltimoMes >= monto):
        return True
    else:
        return False

# Función que aumenta el stock de una materia prima
# Entrada:  [materia] corresponde a la materia prima que se aumentará
#           [cantidad] correponde a la cantidad a aumentar la materia prima
# Salida: Sin valores de retorno
def aumentarMateria(materia, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv') # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    df.loc[df['Materia prima'] == materia, 'Cantidad'] = df.loc[df['Materia prima'] == materia, 'Cantidad'] + cantidad # Se le suma la cantidad de materia prima
    df.to_csv('csv/stock_materia_prima.csv', index=False) # Se guardan los cambios en csv/stock_materia_prima.csv

# Función que reduce el stock de las materias primas
# Entrada:  [materias] corresponde a las materias primas que se reducirán
#           [cantidad] correponde a la cantidad a reducir cada materia prima
# Salida: Sin valores de retorno
def reducirMaterias(materias, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv', index_col=0) # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    for materia in materias:
        df.loc[df['Materia prima'] == materia, 'Cantidad'] = df.loc[df['Materia prima'] == materia, 'Cantidad'] - cantidad # Se le resta la cantidad de materia prima
    df.to_csv('csv/stock_materia_prima.csv', index=False) # Se guardan los cambios en csv/stock_materia_prima.csv

# Función que devuelve el stock faltante de una materia prima
# Entrada:  [materia] corresponde a la materia prima a la que se le debe calcular el stock faltante
#           [cantidad] correponde a la cantidad de materia prima necesaria
# Salida: Devuelve un valor númerico correspondiende al stock faltante, puede ser positivo (falta), negativo (sobra) o 0
def stockFaltanteMateria(materia, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv', index_col=0) # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    filaMateria = df[df['Materia prima'] == materia] # Se busca la materia prima por nombre y se guarda
    stock = filaMateria['Cantidad'].values[0] # Se guarda el stock de esa materia prima
    faltante = cantidad - stock # Se calcula el stock faltante restando lo necesario menos el total
    return faltante

# Función que aumenta el stock de un producto
# Entrada:  [producto] corresponde al producto que se aumentará
#           [cantidad] correponde a la cantidad que se aumentará el producto
# Salida: Sin valores de retorno
def aumentarProducto(producto, cantidad):
    df = pd.read_csv('csv/stock_productos.csv', index_col=0) # Abre el archivo csv/stock_productos.csv y lo guarda en forma de tabla
    df.loc[df['Producto'] == producto, 'Cantidad'] = df.loc[df['Producto'] == producto, 'Cantidad'] + cantidad # Se aumenta el stock del producto en cierta cantidad
    df.to_csv('csv/stock_productos.csv', index=False) # Se guardan los cambios en csv/stock_productos.csv

# Función que disminuye el stock de un producto
# Entrada:  [producto] corresponde al producto que se reducirá
#           [cantidad] correponde a la cantidad a reducir del producto
# Salida: Sin valores de retorno
def reducirProducto(producto, cantidad):
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

while (True):
    menuPrincipal()


    
