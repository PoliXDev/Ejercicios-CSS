    #Eres un profesor y deseas realizar un seguimiento de la asistencia de tus 
#estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y 
#una lista de fechas en las que asistió a clases. Implementa un programa 
#en Python que utilice un diccionario para almacenar la información de las 
#asistencias. El programa debe permitir registrar la asistencia de los 
#estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de 
#estudiantes y las fechas en las que asistieron

#paso 1: crear un diccionario para almacenar la información de las asistencias
asistencias = {}

#paso 2: definir una función para registrar la asistencia de un estudiante
def registrar_asistencia(estudiante, fecha):
    if estudiante not in asistencias:
        asistencias[estudiante] = []
    asistencias[estudiante].append(fecha)
    print(f"Asistencia registrada para {estudiante} el {fecha}.")

#paso 3: definir una función para agregar nuevas fechas de asistencia
def agregar_fecha(estudiante, fecha):
    if estudiante in asistencias:
        asistencias[estudiante].append(fecha)
        print(f"Fecha agregada para {estudiante}: {fecha}.")
    else:
        print(f"El estudiante {estudiante} no está registrado.")

#paso 4: definir una función para mostrar la lista de estudiantes y las fechas en las que asistieron    
def mostrar_asistencias():
    if not asistencias:
        print("No hay estudiantes registrados.")
    else:
        print("\nLista de Estudiantes y Fechas de Asistencia:")
        for estudiante, fechas in asistencias.items():
            print(f"- {estudiante}: {', '.join(fechas)}")

#paso 5: bucle principal para interactuar con el usuario    
while True:
    print("\nMenú:")    
    print("1. Registrar asistencia")
    print("2. Agregar fecha de asistencia")
    print("3. Mostrar lista de asistencias")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        estudiante = input("Ingrese el nombre del estudiante: ")
        fecha = input("Ingrese la fecha de asistencia (dd/mm/aaaa): ")
        registrar_asistencia(estudiante, fecha)
    elif opcion == "2":
        estudiante = input("Ingrese el nombre del estudiante: ")
        fecha = input("Ingrese la fecha de asistencia a agregar (dd/mm/aaaa): ")
        agregar_fecha(estudiante, fecha)
    elif opcion == "3":
        mostrar_asistencias()
    elif opcion == "4":
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

#fin del programa   