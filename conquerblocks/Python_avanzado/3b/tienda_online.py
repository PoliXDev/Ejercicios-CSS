#Crea una clase "Producto" con atributos como nombre, precio y cantidad en 
#stock. Luego, crea una clase "Tienda" que contenga una lista de productos 
#disponibles y métodos para agregar productos, mostrar el inventario y 
#realizar una compra

#clase producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


#clase tienda
class Tienda:
    def __init__(self):
        self.productos = []

#metodo para agregar un producto
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la tienda.")

#metodo para mostrar el inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("No hay productos en la tienda.")
        else:
            print("Inventario de la tienda:")
            for producto in self.productos:
                print(f"- {producto.nombre}: ${producto.precio} - Stock: {producto.stock}")

#metodo para realizar una compra
    def realizar_compra(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(f"Compra realizada de {cantidad} unidades de {nombre_producto}.")
                    return True
        return False
    
#hacer un programa que use esta clase e interactue con el usuario

def main():
    tienda = Tienda()
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Realizar compra")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))
            producto = Producto(nombre, precio, stock)
            tienda.agregar_producto(producto)
        elif opcion == "2":
            tienda.mostrar_inventario()
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a comprar: ")
            cantidad = int(input("Ingrese la cantidad a comprar: "))
            tienda.realizar_compra(nombre_producto, cantidad)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main()