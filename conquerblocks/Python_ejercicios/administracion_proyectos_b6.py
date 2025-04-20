#Eres un gerente de proyectos y necesitas un programa para administrar 
#las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre, 
#una descripción y un responsable asignado. Implementa un programa en 
#Python que utilice un diccionario para almacenar la información de las 
#tareas. El programa debe permitir agregar nuevas tareas, asignar 
#responsables a las tareas existentes, actualizar las descripciones de las 
#tareas y mostrar la lista completa de tareas y responsables.

#paso 1: crear un diccionario para almacenar la información de las tareas
tareas = {} 

#paso 2: definir una función para agregar nuevas tareas
def agregar_tarea(nombre, descripcion, responsable):
    tareas[nombre] = {"descripcion": descripcion, "responsable": responsable}

#paso 3: definir una función para asignar responsables a las tareas existentes      
def asignar_responsable(nombre, responsable):
    if nombre in tareas:
        tareas[nombre]["responsable"] = responsable
    else:
        print(f"La tarea {nombre} no existe.")  

#paso 4: definir una función para actualizar las descripciones de las tareas
def actualizar_descripcion(nombre, descripcion):
    if nombre in tareas:
        tareas[nombre]["descripcion"] = descripcion
    else:
        print(f"La tarea {nombre} no existe.")

#paso 5: definir una función para mostrar la lista completa de tareas y responsables
def mostrar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\nLista de Tareas:")
        for nombre, datos in tareas.items():
            print(f"- {nombre}: {datos['descripcion']} (Responsable: {datos['responsable']})")

#paso 6: bucle principal para interactuar con el usuario    
while True:
    print("\nMenú:")    
    print("1. Agregar tarea")
    print("2. Asignar responsable a una tarea")
    print("3. Actualizar descripción de una tarea")
    print("4. Mostrar lista de tareas")
    print("5. Salir")   

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        responsable = input("Ingrese el responsable de la tarea: ")
        agregar_tarea(nombre, descripcion, responsable) 
    elif opcion == "2":
        nombre = input("Ingrese el nombre de la tarea a la que desea asignar un responsable: ")
        responsable = input("Ingrese el nombre del responsable: ")
        asignar_responsable(nombre, responsable)
    elif opcion == "3":
        nombre = input("Ingrese el nombre de la tarea a la que desea actualizar la descripción: ")
        descripcion = input("Ingrese la nueva descripción de la tarea: ")
        actualizar_descripcion(nombre, descripcion)
    elif opcion == "4":
        mostrar_tareas()
    elif opcion == "5":
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
