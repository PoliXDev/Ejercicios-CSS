#Crea una clase "ListaTareas" que contenga una lista de tareas pendientes. 
#Implementa métodos para agregar una tarea, marcar una tarea como 
#completada y mostrar todas las tareas

#clase lista de tareas
class ListaTareas:
    def __init__(self):
        self.tareas = []
        
#metodo para agregar una tarea
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada a la lista.")

#metodo para marcar una tarea como completada
    def marcar_completada(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"Tarea '{tarea}' marcada como completada.")
        else:
            print(f"Tarea '{tarea}' no encontrada en la lista.") 

#metodo para mostrar todas las tareas
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            print("Tareas pendientes:")
            for tarea in self.tareas:
                print(f"- {tarea}") 

#hacer un programa que use esta clase e interactue con el usuario

def main():
    lista = ListaTareas()
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Salir")
#pedir al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")
#condicionales para ejecutar las opciones
        if opcion == "1":
            tarea = input("Ingrese la tarea: ")
            lista.agregar_tarea(tarea)
        elif opcion == "2":
            tarea = input("Ingrese la tarea a marcar como completada: ")
            lista.marcar_completada(tarea)
        elif opcion == "3":
            lista.mostrar_tareas()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main()