#Tienes una tienda y deseas realizar un seguimiento de las ventas diarias 
#de tus productos. Cada producto tiene un nombre y una cantidad 
#vendida. Implementa un programa en Python que utilice un diccionario 
#para almacenar la información de las ventas. El programa debe permitir 
#registrar las ventas de productos, actualizar la cantidad vendida de un 
#   producto existente y calcular el total de ventas diarias , y lista de productos vendidos

#paso 1: crear un diccionario para almacenar la información de las ventas
ventas = {}

#paso 2: definir una función para registrar las ventas de un producto
def registrar_venta(producto, cantidad):
    if producto in ventas:
        ventas[producto] += cantidad
    else:
        ventas[producto] = cantidad

#paso 3: definir una función para actualizar la cantidad vendida de un producto existente
def actualizar_venta(producto, cantidad):
    if producto in ventas:
        ventas[producto] += cantidad  
    else:
        print(f"El producto {producto} no existe en el registro de ventas.") 

#paso 4: definir una función para calcular el total de ventas diarias
def calcular_total_ventas():
    return sum(ventas.values())

#paso 5: definir una función para mostrar el menú principal
def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Agregar venta")
    print("2. Ver total de ventas")
    print("3. Ver promedio de ventas")
    print("4. Ver lista de ventas") 
    print("5. Salir")
# paso 6: definir una función para ver la lista de ventas
def ver_lista_ventas(ventas):
    if not ventas:
        print("No hay ventas registradas.")
    else:
        print("\nLista de Ventas:")
        for producto, cantidad in ventas.items():
            print(f"{producto}: {cantidad}")

# paso 7: calcular el promedio de ventas
def calcular_promedio_ventas():
    if not ventas:
        return 0
    return sum(ventas.values()) / len(ventas)

#paso 8: bucle principal para interactuar con el usuario
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad vendida: "))
                if cantidad <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, ingrese un número entero positivo.")
        registrar_venta(producto, cantidad)
    elif opcion == "2":
        total = calcular_total_ventas()
        print(f"El total de ventas diarias es: {total}")
    elif opcion == "3":
        promedio = calcular_promedio_ventas()
        print(f"El promedio de ventas es: {promedio:.2f}")
    elif opcion == "4":
        ver_lista_ventas(ventas)
    elif opcion == "5":
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
