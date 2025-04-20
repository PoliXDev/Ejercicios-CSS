"""optimisacion de subarreglo: desarrollaruna funcion llamada max_subarray que encuentre y devulva la suma maxima del sub arreglo
contiguo en la con la suma maxima en la lista , [1, -2,3,10,-4, 7,2 , -5] y el subarreglo contiguo con la suma maxima es [3,10,-4, 7,2] 
y la suma de esos numeros es 18"""

def max_subarray(nums):
    suma_maxima = float('-inf')
    suma_actual = 0
    inicio = 0
    fin = 0
    inicio_temporal = 0
    
    for i, num in enumerate(nums):
        if suma_actual <= 0:
            suma_actual = num
            inicio_temporal = i
        else:
            suma_actual += num
            
        if suma_actual > suma_maxima:
            suma_maxima = suma_actual
            inicio = inicio_temporal
            fin = i
            
    return suma_maxima, nums[inicio:fin + 1]

# Arreglo original
nums = [1, -2, 3, 10, -4, 7, 2, -5]
print("Arreglo original:", nums)

# Obtener resultados
suma_maxima, subarreglo = max_subarray(nums)
print("Subarreglo contiguo con suma máxima:", subarreglo)
print("Suma máxima:", suma_maxima)

