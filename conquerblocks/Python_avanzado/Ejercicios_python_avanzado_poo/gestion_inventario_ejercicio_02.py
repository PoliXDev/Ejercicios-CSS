"""Desarrollar un sistema de gestion de inventario, donde el inventario esta representado
por una lista de productos ordenados por sus codigos . cada producto se describe como un diccionario
con las claves codigo y cantidad , implementar una funcion recursiva que realize una busqueda binaria en este inventario
y devuelva la cantidad disponible de un producto dado su codigo """

def busqueda_binaria(inventario, codigo, izquierda, derecha):
    if izquierda > derecha:
        return 0
    medio = (izquierda + derecha) // 2
    if inventario[medio]["codigo"] == codigo:
        return inventario[medio]["cantidad"]
    elif inventario[medio]["codigo"] > codigo:
        return busqueda_binaria(inventario, codigo, izquierda, medio - 1)
    else:
        return busqueda_binaria(inventario, codigo, medio + 1, derecha)

inventario = [
    {"codigo": 1, "cantidad": 10},
    {"codigo": 2, "cantidad": 20},
    {"codigo": 3, "cantidad": 30},
]

print(busqueda_binaria(inventario, 2, 0, len(inventario) - 1))  

#programa para interactuar con el usuario y realizar las operaciones de inventario

def main():
    inventario = [
        {"codigo": 1, "cantidad": 10},
        {"codigo": 2, "cantidad": 20},
        {"codigo": 3, "cantidad": 30},
    ]   
    while True:
        print("\nMenu:")
        print("1. Buscar producto")
        print("2. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            codigo = int(input("Ingrese el codigo del producto: "))
            cantidad = busqueda_binaria(inventario, codigo, 0, len(inventario) - 1)
            print(f"Cantidad disponible: {cantidad}")
        elif opcion == "2":
            break

main()      