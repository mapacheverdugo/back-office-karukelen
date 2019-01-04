# IMPORTACIÓN_DE_FUNCIONES

import inventario
import produccion
import ventas
import compras

# DEFINICIÓN_DE_FUNCIONES

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
        inventario.menu()
    elif (opcion == 2):
        produccion.menu()
    elif (opcion == 3):
        ventas.menu()
    elif (opcion == 4):
        print("Compras seleccionado")
    else:
        print("Error, no existe la opción seleccionada")

menuPrincipal()


    
