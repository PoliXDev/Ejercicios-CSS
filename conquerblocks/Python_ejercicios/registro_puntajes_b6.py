#implementa un programa en Python que permita registrar y mantener un 
#seguimiento de los puntajes de un juego. El programa debe permitir a los 
#jugadores ingresar sus nombres y puntajes, almacenarlos en un 
#diccionario y proporcionar funcionalidades para mostrar el puntaje más 
#alto, el promedio de puntajes y la cantidad total de jugadores

#definir un diccionario para almacenar los puntajes
puntajes = {}   

# paso 1: definir una función para registrar los puntajes
def registrar_puntaje(nombre, puntaje):
    if nombre not in puntajes:  
        puntajes[nombre] = puntaje
        print(f"Puntaje registrado para {nombre}: {puntaje}.")
    else:
        print(f"El jugador {nombre} ya tiene un puntaje registrado.")

#paso 2: definir una función para mostrar el puntaje más alto
def mostrar_puntaje_mas_alto():
    if not puntajes:    
        print("No hay puntajes registrados.")
    else:
        nombre_mas_alto = max(puntajes, key=puntajes.get)
        print(f"El puntaje más alto es de {nombre_mas_alto} con {puntajes[nombre_mas_alto]} puntos.")   

#paso 3: definir una función para calcular el promedio de puntajes
def calcular_promedio_puntajes():
    if not puntajes:
        print("No hay puntajes registrados.")
    else:
        total_puntajes = sum(puntajes.values())
        cantidad_jugadores = len(puntajes)
        promedio = total_puntajes / cantidad_jugadores
        print(f"El promedio de puntajes es de {promedio:.2f} puntos.")

#paso 4: definir una función para mostrar la cantidad total de jugadores
def mostrar_cantidad_jugadores():
    cantidad_jugadores = len(puntajes)
    print(f"La cantidad total de jugadores es de {cantidad_jugadores}.")

#paso 5: bucle principal para interactuar con el usuario
while True: 
    print("\nMenú:")
    print("1. Registrar puntaje")
    print("2. Mostrar puntaje más alto")
    print("3. Calcular promedio de puntajes")
    print("4. Mostrar cantidad de jugadores")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")   

    if opcion == "1":
        nombre = input("Ingrese el nombre del jugador: ")                   
        puntaje = int(input("Ingrese el puntaje del jugador: "))
        registrar_puntaje(nombre, puntaje)
    elif opcion == "2":
        mostrar_puntaje_mas_alto()
    elif opcion == "3":
        calcular_promedio_puntajes()
    elif opcion == "4":
        mostrar_cantidad_jugadores()
    elif opcion == "5": 
        print("¡Gracias por usar el programa!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")