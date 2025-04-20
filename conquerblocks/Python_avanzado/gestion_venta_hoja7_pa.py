#Crea un programa que permita gestionar las ventas de una tienda. Utiliza una 
#estructura de datos adecuada para almacenar la información de las ventas 
#(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para 
#agregar el producto vendido con su precio y otro para mostrar las ventas de 
#productos con sus respectivos precios.
#(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”: 
#precio1}, {“Producto”: producto2, “Precio”: precio2}…])

#paso 1: crear una lista de diccionarios para almacenar la información de las ventas
ventas = []

#paso 2: definir una función para agregar el producto vendido con su precio
def agregar_venta(producto, precio):
    ventas.append({"Producto": producto, "Precio": precio})


#paso 3: definir una función para mostrar las ventas de productos con sus respectivos precios
def mostrar_ventas():
    for venta in ventas:
        print(f"Producto: {venta['Producto']}, Precio: {venta['Precio']}")

#paso 4: mostrar el menú principal
def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Agregar venta")
    print("2. Mostrar ventas")
    print("3. Salir")

#paso 5: ejecutar el programa
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        producto = input("Ingrese el producto: ")
        precio = float(input("Ingrese el precio: "))
        agregar_venta(producto, precio)
    elif opcion == "2":
        mostrar_ventas()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


b