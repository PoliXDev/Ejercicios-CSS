"""crear un sistema de laberintos, esta representado por una matriz, donde ciertos valores representanlos caminos permitidos (0) paredes,paredes(1) y la salida (9)
implementar una funcion recursiva la rutapara encontrar la salida del laberinto
1. implementar funcion (resolver_laberinto) usando recursividad 
2. la funcion debe devolver una lista de coordenadas que representan el camino para llegar a la salida del laberinto
3. lista de movimientos : arriba (-1, 0) , abajo (1, 0) , izquierda (0, -1) , derecha (0, 1)"""

def resolver_laberinto(laberinto, inicio, fin, camino=None, visitados=None):
    if camino is None:
        camino = []
    if visitados is None:
        visitados = set()
    
    fila, columna = inicio
    
    # Verificar si estamos fuera del laberinto o en una pared
    if (fila < 0 or fila >= len(laberinto) or 
        columna < 0 or columna >= len(laberinto[0]) or 
        laberinto[fila][columna] == 1 or 
        (fila, columna) in visitados):
        return None
    
    # Agregar posición actual al camino y a visitados
    camino.append((fila, columna))
    visitados.add((fila, columna))
    
    # Si llegamos a la salida (9), retornamos el camino
    if laberinto[fila][columna] == 9:
        return camino
    
    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Probar cada movimiento posible
    for mov_fila, mov_col in movimientos:
        nueva_fila = fila + mov_fila
        nueva_col = columna + mov_col
        
        resultado = resolver_laberinto(laberinto, 
                                     (nueva_fila, nueva_col), 
                                     fin, 
                                     camino[:], 
                                     visitados.copy())
        if resultado:
            return resultado
    
    return None

def imprimir_laberinto_con_solucion(laberinto, solucion):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if (i, j) in solucion:
                print("*", end=" ")
            elif laberinto[i][j] == 1:
                print("█", end=" ")
            elif laberinto[i][j] == 9:
                print("S", end=" ")
            else:
                print("·", end=" ")
        print()

# Ejemplo de uso:
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 9]
]

inicio = (0, 0)  # Posición inicial
fin = (4, 4)     # Posición final

solucion = resolver_laberinto(laberinto, inicio, fin)
if solucion:
    print("Camino encontrado:", solucion)
    print("\nRepresentación gráfica del laberinto:")
    print("* = camino, █ = pared, S = salida, · = espacio libre\n")
    imprimir_laberinto_con_solucion(laberinto, solucion)
else:
    print("No hay solución")



