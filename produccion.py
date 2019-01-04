import pandas as pd

def menu():
    opcion = 0
    while (opcion < 1 or opcion > 4):
        print("\n¿Qué acción desea realizar?\n")
        print("1. Recepcionar y mostrar pedidos\n")
        print("2. Procesar pedido\n")
        print("3. Mostrar a los n pedidos de mayor utilidad")
        print("4. Mostrar al comprador que más aporta")
        opcion = eval(input("Ingrese la opción seleccionada: "))
    
    if (opcion == 1):
        print("Calcular capital seleccionado")
    elif (opcion == 2):
        print("Calcular capital seleccionado")
    elif (opcion == 3):
        print("Calcular capital seleccionado")
    elif (opcion == 4):
        print("Calcular capital seleccionado")
    else:
        print("Error, no existe la opción seleccionada")

def pedidosAListas():
    df = pd.read_csv('pedidos.csv')
    
    for index, fila in df.iterrows():
        print(fila['Cliente'])

pedidosAListas()