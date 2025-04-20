"""empresa de comercio electrónico y tienes
información detallada sobre las ventas de productos. Cada venta se representa
como un diccionario, que incluye el nombre del producto, la fecha de venta, el
monto de la venta y la ubicación del comprador. Realiza un análisis avanzado
de estas ventas.
Python avanzado - ejercicios 4
1. Filtra las ventas realizadas en el último trimestre del año.
2. Selecciona solo las ventas de productos con un monto superior a $500.
3. Agrupa las ventas por ubicación del comprador.
4. Calcula el promedio del monto de venta para cada ubicación.
5. Ordena las ubicaciones por el promedio del monto de venta de forma
descendente. Utiliza funciones lambda."""

from datetime import datetime

ventas = [
    {"producto": "Laptop", "fecha": "2023-01-15", "monto": 800, "ubicacion": "Nueva York"},
    {"producto": "Smartphone", "fecha": "2023-02-20", "monto": 600, "ubicacion": "Los Ángeles"},
    {"producto": "Tablet", "fecha": "2023-03-10", "monto": 400, "ubicacion": "Chicago"},
    {"producto": "Smartwatch", "fecha": "2023-04-05", "monto": 300, "ubicacion": "Nueva York"},
    {"producto": "Monitor", "fecha": "2023-05-15", "monto": 550, "ubicacion": "Los Ángeles"},
    {"producto": "Mouse", "fecha": "2023-06-25", "monto": 250, "ubicacion": "Chicago"},
    {"producto": "Teclado", "fecha": "2023-07-10", "monto": 150, "ubicacion": "Nueva York"},
    {"producto": "Altavoces", "fecha": "2023-08-15", "monto": 350, "ubicacion": "Los Ángeles"},
    {"producto": "Cargador", "fecha": "2023-09-20", "monto": 100, "ubicacion": "Chicago"}
]

# 1. Filtra las ventas realizadas en el último trimestre del año.
def obtener_ultimo_trimestre(fecha_str):
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    return fecha.month >= 10 and fecha.month <= 12
ventas_ultimo_trimestre = [venta for venta in ventas if obtener_ultimo_trimestre(venta["fecha"])]

# Mostrar resultados del último trimestre
print("\n=== Ventas del último trimestre ===")
for venta in ventas_ultimo_trimestre:
    print(f"Producto: {venta['producto']:<15} Fecha: {venta['fecha']} Monto: ${venta['monto']:>6}")

# 2. Selecciona solo las ventas de productos con un monto superior a $500.
ventas_monto_superior_a_500 = [venta for venta in ventas if venta["monto"] > 500]

# Mostrar ventas superiores a $500
print("\n=== Ventas superiores a $500 ===")
for venta in ventas_monto_superior_a_500:
    print(f"Producto: {venta['producto']:<15} Monto: ${venta['monto']:>6} Ubicación: {venta['ubicacion']}")

# 3. Agrupa las ventas por ubicación del comprador.
ventas_por_ubicacion = {}
for venta in ventas:
    ubicacion = venta["ubicacion"]
    if ubicacion not in ventas_por_ubicacion:
        ventas_por_ubicacion[ubicacion] = []    
    ventas_por_ubicacion[ubicacion].append(venta)

# 4. Calcula el promedio del monto de venta para cada ubicación.
promedio_ventas_por_ubicacion = {ubicacion: sum(venta["monto"] for venta in ventas_por_ubicacion[ubicacion]) / len(ventas_por_ubicacion[ubicacion]) for ubicacion in ventas_por_ubicacion}

# Mostrar promedios por ubicación
print("\n=== Promedio de ventas por ubicación ===")
for ubicacion, promedio in promedio_ventas_por_ubicacion.items():
    print(f"Ubicación: {ubicacion:<15} Promedio: ${promedio:.2f}")

# 5. Ordena las ubicaciones por el promedio del monto de venta de forma descendente. Utiliza funciones lambda.
ubicaciones_ordenadas = sorted(promedio_ventas_por_ubicacion, key=lambda x: promedio_ventas_por_ubicacion[x], reverse=True)

# Mostrar ubicaciones ordenadas
print("\n=== Ubicaciones ordenadas por promedio de ventas ===")
for ubicacion in ubicaciones_ordenadas:
    print(f"{ubicacion:<15} ${promedio_ventas_por_ubicacion[ubicacion]:.2f}")


    
