# Escribe una funcionque solicite dos números. Suma los números y muestra el resultado. 
# Captura el ValueError si alguno de los valores de entrada no es un número e imprime un mensaje de error amigable  y usa bucle while para continuar
# solicitando números hasta que se introduzcan dos números válidos.

def suma_numeros():
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            resultado = num1 + num2
            print(f"La suma de {num1} y {num2} es {resultado}")
            break
        except ValueError:
            print("Error: Introduce un número válido.")

suma_numeros()


