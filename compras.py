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
    while (opcion < 0 or opcion > 3):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Ver materias disponibles para comprar\n")
        print("2. Ver proveedor más conveniente\n")
        print("3. Comprar materia prima más conveniente\n")
        print("0. Volver al menú principal\n")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        verMateriasDisponibles()
        menu()
    elif (opcion == 2):
        cotizarMateria()
        menu()
    elif (opcion == 3):
        comprarMateriaPrima()
        menu()

def verMateriasDisponibles():
    listaSinRepetir = []
    materiasPrimas = listaDeMaterias()
    for i, proveedor in enumerate(materiasPrimas):
        for tupla in proveedor:
            nombre = tupla[0]
            if (nombre not in listaSinRepetir):
                listaSinRepetir.append(nombre)
    
    for index, materia in enumerate(listaSinRepetir):
        print(str(index + 1) + '. ' + materia)
    
    return listaSinRepetir

def cotizarMateria():
    lista = verMateriasDisponibles()
    numeroMateria = eval(input("Ingrese la materia que desea cotizar: ")) # Se le pide al usuario que ingrese el número de pedido
    materiaACotizar = lista[numeroMateria - 1]
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
    precioMenorUnidad = -1
    indiceProveedor = -1
    nombreProveedor = ''
    unidadMenor = -1

    materiasPrimas = listaDeMaterias()
    for i, proveedor in enumerate(materiasPrimas):
        for tupla in proveedor:
            nombre = tupla[0]
            unidades = eval(tupla[1])
            precio = tupla[2]
            if (nombre == materia):
                precioPorUnidad = precio / unidades
                if (precioMenorUnidad == -1 or precioMenorUnidad > precioPorUnidad):
                    precioMenorUnidad = precioPorUnidad
                    indiceProveedor = i
                    nombreProveedor = obtenerProveedor(i)
                    unidadMenor = unidades
    return (indiceProveedor, nombreProveedor, precioMenorUnidad, unidadMenor)

def comprarMateriaPrima():
    materias = verMateriasDisponibles()
    
    numeroMateria = eval(input("Ingrese la materia que desea comprar: ")) # Se le pide al usuario que ingrese un valor
    cantidad = eval(input("Ingrese cuantas promociones desea comprar: "))

    materiaAComprar = materias[numeroMateria - 1]
    proveedor = proveedorMasConveniente(materiaAComprar)
    unidadesEnPromocion = proveedor[3]

    aumentarMateria(materiaAComprar, unidadesEnPromocion * cantidad)

def aumentarMateria(materia, cantidad):
    df = pd.read_csv('csv/stock_materia_prima.csv') # Abre el archivo csv/stock_materia_prima.csv y lo guarda en forma de tabla
    df.loc[df['Materia prima'] == materia, 'Cantidad'] = df.loc[df['Materia prima'] == materia, 'Cantidad'] + cantidad # Se le resta la cantidad de materia prima
    df.to_csv('csv/stock_materia_prima.csv', index=False) # Se guardan los cambios en csv/stock_productos.csv