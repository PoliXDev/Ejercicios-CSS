"""Imagina que estás desarrollando un sistema complejo que incluye múltiples
funciones críticas. Para asegurarte de que todo funcione correctamente y para
realizar un seguimiento del tiempo de ejecución de estas funciones, decides
implementar un decorador de registro (logger) con tiempo de ejecución.
El decorador debería realizar las siguientes acciones:
1. Antes de llamar a la función original (puedes incluir cualquier función),
debe imprimir un mensaje indicando que la función está a punto de
ejecutarse.
2. Después de que la función se haya ejecutado, debe imprimir un mensaje
que incluya el tiempo que tardó la función en ejecutarse.
3. Si la función original arroja una excepción, el decorador debe manejarla e
imprimir un mensaje adecuado, indicando que se ha producido una
excepción.
"""

import time

def logger_tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        print(f"Ejecutando {func.__name__}...")
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} ejecutada en {end_time - start_time:.2f} segundos")
            return result
        except Exception as e:
            print(f"Error en {func.__name__}: {e}")
            raise
    return wrapper

@logger_tiempo_ejecucion
def serie_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Implementación iterativa más eficiente
    a, b = 0, 1
    secuencia = [a, b]  # Lista para almacenar la secuencia
    
    for _ in range(2, n + 1):
        a, b = b, a + b
        secuencia.append(b)  # Agregamos cada número a la secuencia
    
    # Mostramos los números de la secuencia
    print("Secuencia de Fibonacci:")
    for i, num in enumerate(secuencia):
        print(f"F({i}) = {num}")
    
    return b

print(serie_fibonacci(20))