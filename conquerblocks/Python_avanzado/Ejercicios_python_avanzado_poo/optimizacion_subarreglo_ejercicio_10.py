"""estoy trabajando en un sistema de análisis de datos y me han proporcionado una lista de números enteros. 
Tu tarea es desarrollar una función llamada max_subarray_sum que encuentre y devuelva la suma máxima de
un subarreglo contiguo en la lista.
Por ejemplo, considera la lista [1, -2, 3, 10, -4, 7, 2, -5] . El subarreglo
contiguo con la suma máxima es [3, 10, -4, 7, 2] , y la suma de esos elementos
es 18 . Por lo tanto, la función debería devolver 18 para esta lista.
Implementa la función max_subarray_sum y, además, aplica memoización para
mejorar su eficiencia en el cálculo de subarreglos de suma máxima en listas
previamente procesadas."""

import functools

#decorador para aplicar memoizacion
@functools.lru_cache(maxsize=None)
def max_subarray_sum(lista_tupla):
    max_sum = float('-inf') 
    current_sum = 0
    
    #algoritmo de kadane
    for num in lista_tupla:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Ejemplos de uso
if __name__ == "__main__":
    # Convertimos las listas a tuplas antes de llamar a la función
    lista1 = tuple([1, -2, 3, 10, -4, 7, 2, -5])
    print(f"Suma máxima del subarreglo en {lista1}: {max_subarray_sum(lista1)}")
    
    lista2 = tuple([-2, -3, 4, -1, -2, 1, 5, -3])
    print(f"Suma máxima del subarreglo en {lista2}: {max_subarray_sum(lista2)}")
    
    lista3 = tuple([-1, -2, -3, -4])
    print(f"Suma máxima del subarreglo en {lista3}: {max_subarray_sum(lista3)}")