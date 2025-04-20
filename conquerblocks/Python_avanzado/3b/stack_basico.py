#Crea una clase "Pila" que represente una pila (stack) básica. Implementa 
#métodos para agregar elementos a la pila, quitar elementos y mostrar el 
#contenido actual.

#clase pila
class Pila:
    def __init__(self): 
        self.items = []

#metodo para agregar un elemento a la pila
    def agregar_elemento(self, elemento):
        self.items.append(elemento)
        print(f"Elemento '{elemento}' agregado a la pila.")

#metodo para quitar un elemento de la pila
    def quitar_elemento(self):
        if not self.items:
            print("La pila está vacía. No se puede quitar ningún elemento.")
        else:
            return self.items.pop()

#metodo para mostrar el contenido actual de la pila
    def mostrar_contenido(self):
        if not self.items:
            print("La pila está vacía.")
        else:
            print("Contenido de la pila:")
            for item in self.items:
                print(f"- {item}")

#ejemplo de uso
pila = Pila()
pila.agregar_elemento("Elemento 1")
pila.agregar_elemento("Elemento 2")
pila.mostrar_contenido()
pila.quitar_elemento()
pila.mostrar_contenido()

