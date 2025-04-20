"""estás trabajando en un sistema de análisis de texto que requiere
calcular la frecuencia de ocurrencia de palabras en un conjunto de
documentos. Implementa una función llamada calcular_frecuencia_palabras que
tome como entrada un texto y devuelva un diccionario que muestre la
frecuencia de cada palabra en el texto.
1. La función debe ser capaz de manejar textos y ser insensible a
mayúsculas/minúsculas (por ejemplo, "Hola" y "hola" se consideran la
misma palabra).
2. Se deben excluir las palabras comunes (artículos, preposiciones, etc.) que
no aportan información relevante al análisis.
3. Utiliza memoización para evitar recalcular la frecuencia de palabras para el
mismo texto"""

import functools
import re
import time

# Función con memoización
@functools.lru_cache(maxsize=None)
def calcular_frecuencia_palabras_memo(texto):
    palabras = texto.lower().split()    
    palabras = [re.sub(r'[^a-z]', '', palabra) for palabra in palabras]
    palabras = [palabra for palabra in palabras if palabra and len(palabra) > 2]
    
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia

# Función sin memoización
def calcular_frecuencia_palabras_sin_memo(texto):
    palabras = texto.lower().split()    
    palabras = [re.sub(r'[^a-z]', '', palabra) for palabra in palabras]
    palabras = [palabra for palabra in palabras if palabra and len(palabra) > 2]
    
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia

# Función para medir tiempo
def medir_tiempo(texto, repeticiones=1000):
    # Medición con memoización
    inicio = time.time()
    for _ in range(repeticiones):
        calcular_frecuencia_palabras_memo(texto)
    tiempo_memo = time.time() - inicio
    
    # Medición sin memoización
    inicio = time.time()
    for _ in range(repeticiones):
        calcular_frecuencia_palabras_sin_memo(texto)
    tiempo_sin_memo = time.time() - inicio
    
    return tiempo_memo, tiempo_sin_memo

# Ejemplo de uso
texto1 = "Hola, ¿cómo estás? ¿Qué tal el día?"
texto2 = "El sol se puso y la luna salió"

# Mostrar resultados
print("Resultados del análisis:")
print(f"Texto 1: {calcular_frecuencia_palabras_memo(texto1)}")
print(f"Texto 2: {calcular_frecuencia_palabras_memo(texto2)}")

# Medir tiempos
tiempo_memo, tiempo_sin_memo = medir_tiempo(texto1)
print("\nComparación de tiempos (1000 repeticiones):")
print(f"Con memoización: {tiempo_memo:.4f} segundos")
print(f"Sin memoización: {tiempo_sin_memo:.4f} segundos")
print(f"Diferencia: {tiempo_sin_memo - tiempo_memo:.4f} segundos")