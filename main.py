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

import inventario
import produccion
import ventas
import compras

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
        inventario.menu()
    elif (opcion == 2):
        produccion.menu()
    elif (opcion == 3):
        ventas.menu()
    elif (opcion == 4):
        print("Compras seleccionado")
    else:
        print("Error, no existe la opción seleccionada")

while (True):
    menuPrincipal()


    
