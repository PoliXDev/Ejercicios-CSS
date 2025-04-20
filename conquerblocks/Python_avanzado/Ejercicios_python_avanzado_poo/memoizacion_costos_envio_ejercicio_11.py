"""sistema de gestión de costos de envío para
una empresa de logística. El sistema debe calcular el costo de envío para
diferentes destinos, distancias y pesos de paquetes. Implementa una función
llamada calcular_costo_envio que tome como entrada un destino, una distancia
en kilómetros y un peso en kilogramos, y devuelva el costo total del envío.
Requerimientos:
1. El costo base de envío es de $5.0.
2. El costo por kilómetro de distancia es de $0.1.
3. El costo por kilogramo de peso es de $0.2.
Implementa la función de manera eficiente utilizando memoización para evitar
recalcular el costo para los mismos destinos, distancias y pesos."""

import functools
import time

@functools.lru_cache(maxsize=None)
def calcular_costo_envio(destino, distancia, peso):
    # Definir los costos base
    costo_base = 5.0
    costo_por_km = 0.1
    costo_por_kg = 0.2
    
    return costo_base + (costo_por_km * distancia) + (costo_por_kg * peso)

print(calcular_costo_envio("Lima", 100, 10))

def calcular_distancia_sin_memo(ciudad_actual, ciudades_restantes):
    if not ciudades_restantes:
        return 0
    
    return min(
        distancias[ciudad_actual][siguiente_ciudad] + 
        calcular_distancia_sin_memo(siguiente_ciudad, ciudades_restantes - {siguiente_ciudad})
        for siguiente_ciudad in ciudades_restantes
    )

@functools.lru_cache(maxsize=None)
def calcular_distancia_con_memo(ciudad_actual, ciudades_restantes):
    if not ciudades_restantes:
        return 0
    
    return min(
        distancias[ciudad_actual][siguiente_ciudad] + 
        calcular_distancia_con_memo(siguiente_ciudad, frozenset(ciudades_restantes - {siguiente_ciudad}))
        for siguiente_ciudad in ciudades_restantes
    )

# Ejemplo de uso con ciudades
if __name__ == "__main__":
    # Definir distancias entre ciudades
    distancias = {
        'A': {'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30}
    }
    
    # Conjunto de ciudades a visitar
    ciudades = {'B', 'C', 'D'}
    ciudad_inicio = 'A'
    
    # Medir tiempo sin memoización
    inicio = time.time()
    resultado_sin_memo = calcular_distancia_sin_memo(ciudad_inicio, ciudades)
    tiempo_sin_memo = time.time() - inicio
    
    # Medir tiempo con memoización
    inicio = time.time()
    resultado_con_memo = calcular_distancia_con_memo(ciudad_inicio, frozenset(ciudades))
    tiempo_con_memo = time.time() - inicio
    
    print(f"Distancia mínima: {resultado_sin_memo}")
    print(f"Tiempo sin memoización: {tiempo_sin_memo:.6f} segundos")
    print(f"Tiempo con memoización: {tiempo_con_memo:.6f} segundos")