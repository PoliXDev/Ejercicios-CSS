#magina que eres el gerente de recursos humanos de una empresa y 
#necesitas gestionar la información de los empleados. Cada empleado 
#tiene un nombre, salario y departamento al que pertenece. Implementa 
#un programa en Python que permita agregar nuevos empleados, 
#actualizar el salario de un empleado existente, mostrar la lista completa 
#de empleados y calcular el promedio salarial por departamento.

#paso 1: crear un diccionario para almacenar la información de los empleados
empleados = {}

#paso 2: definir una función para agregar nuevos empleados
def agregar_empleado(nombre, salario, departamento):
    empleados[nombre] = {"salario": salario, "departamento": departamento}  

#paso 3: definir una función para actualizar el salario de un empleado existente
def actualizar_salario(nombre, salario):
    if nombre in empleados:
        empleados[nombre]["salario"] = salario  
    else:
        print(f"El empleado {nombre} no existe.")

#paso 4: definir una función para mostrar la lista completa de empleados
def mostrar_empleados():
    if not empleados:
        print("No hay empleados registrados.")
    else:
        print("\nLista de Empleados:")
        for nombre, datos in empleados.items():
            print(f"- {nombre}: Salario: {datos['salario']}, Departamento: {datos['departamento']}")

#paso 5: definir una función para calcular el promedio salarial por departamento
def calcular_promedio_salarial(departamento):
    if not empleados:               
        return 0
    else:
        total_salarios = sum(datos["salario"] for datos in empleados.values() if datos["departamento"] == departamento)
        cantidad_empleados = len([datos for datos in empleados.values() if datos["departamento"] == departamento])
    return total_salarios / cantidad_empleados

#paso 6: bucle principal para interactuar con el usuario
while True: 
    print("\nMenú:")
    print("1. Agregar empleado")
    print("2. Actualizar salario")  
    print("3. Mostrar empleados")
    print("4. Calcular promedio salarial por departamento")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")   

    if opcion == "1":     
        nombre = input("Ingrese el nombre del empleado: ")
        salario = float(input("Ingrese el salario del empleado: "))
        departamento = input("Ingrese el departamento del empleado: ")
        agregar_empleado(nombre, salario, departamento)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado a actualizar: ")
        salario = float(input("Ingrese el nuevo salario del empleado: "))
        actualizar_salario(nombre, salario)
    elif opcion == "3":
        mostrar_empleados()
    elif opcion == "4":
        departamento = input("Ingrese el departamento para calcular el promedio salarial: ")
        promedio = calcular_promedio_salarial(departamento)
        print(f"El promedio salarial en el departamento {departamento} es de ${promedio:.2f}")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")  

#fin del programa