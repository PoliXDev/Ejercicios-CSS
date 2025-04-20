#Supongamos que tienes los resultados de una elección con los nombres 
#de los candidatos y la cantidad de votos obtenidos por cada uno. 
#Implementa un programa en Python que permita registrar los votos, 
#mostrar la lista completa de candidatos y sus votos, encontrar al 
#candidato ganador (con más votos) y calcular el porcentaje de votos que 
#obtuvo cada candidato

#paso 1: crear un diccionario para almacenar los resultados de la elección
resultados = {} 

#paso 2: definir una función para registrar votos
def registrar_voto(candidato, votos):
    if candidato in resultados:
        resultados[candidato] += votos
    else:
        resultados[candidato] = votos   

#paso 3: definir una función para mostrar la lista completa de candidatos y sus votos
def mostrar_resultados():
    if not resultados:
        print("No hay resultados registrados.")
    else:
        print("\nResultados de la elección:")
        for candidato, votos in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
            print(f"- {candidato}: {votos} votos")

#paso 4: definir una función para encontrar el candidato ganador    
def encontrar_ganador():
    if not resultados:
        return None
    else:
        return max(resultados, key=resultados.get)  

#paso 5: definir una función para calcular el porcentaje de votos de cada candidato 
def calcular_porcentaje_votos(candidato):
    if candidato in resultados:
        return (resultados[candidato] / sum(resultados.values())) * 100
    else:
        return 0    

#paso 6: bucle principal para interactuar con el usuario    
while True:
    print("\nMenú:")
    print("1. Registrar voto")
    print("2. Mostrar resultados")
    print("3. Encontrar ganador")
    print("4. Calcular porcentaje de votos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        candidato = input("Ingrese el nombre del candidato: ")
        votos = int(input("Ingrese la cantidad de votos: "))
        registrar_voto(candidato, votos)
    elif opcion == "2":
        mostrar_resultados()
    elif opcion == "3":
        ganador = encontrar_ganador()
        if ganador:
            print(f"\nEl candidato ganador es: {ganador}")
        else:
            print("No hay resultados registrados.")
    elif opcion == "4":
        candidato = input("Ingrese el nombre del candidato: ")  
        porcentaje = calcular_porcentaje_votos(candidato)
        print(f"\nEl candidato {candidato} obtuvo el {porcentaje:.2f}% de los votos.")
    elif opcion == "5":
        print("¡Gracias por usar el sistema de análisis de votaciones!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

#fin del programa
