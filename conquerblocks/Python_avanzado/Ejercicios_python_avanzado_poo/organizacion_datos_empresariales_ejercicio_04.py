"""Tenemos una empresa internacional con equipos en diferentes paises, cada equipo tiene una lista de empleados, representados como diccionarios con informacion , nombre , edad y rendimiento en proyectos  recientes
hay que organizar una lista consolidada de todos los empleados de la empresa, con las siguientes reglas:
1. se debe ordenar por rendiemiento en proyectos recientes de forma descendente.
2. para aquellos con el  mismo rendimiento se debe ordenar por edad de forma ascendente
3. agrupar por pais para un analisis mas efectivo
utilizar funciones lambda para la resolucion del ejercicio."""

#importar la libreria groupby
from itertools import groupby

#funcion para ordenar los empleados por rendimiento y edad
def ordenar_empleados(empleados):
    return sorted(empleados, key=lambda x: (-x['rendimiento'], x['edad']))

#funcion para agrupar los empleados por pais
def agrupar_por_pais(empleados):
    return groupby(empleados, key=lambda x: x['pais'])

#funcion para mostrar los empleados ordenados por pais
def mostrar_empleados_ordenados(empleados):
    for pais, grupo in agrupar_por_pais(empleados):
        print(f"Equipo de {pais}:")
        for empleado in ordenar_empleados(grupo):
            print(f" - {empleado['nombre']} ({empleado['edad']} años, {empleado['rendimiento']} de rendimiento)")

#lista de empleados
empleados = [
    {'nombre': 'Juan', 'edad': 30, 'pais': 'España', 'rendimiento': 85},
    {'nombre': 'Ana', 'edad': 25, 'pais': 'Francia', 'rendimiento': 90},
    {'nombre': 'Luis', 'edad': 35, 'pais': 'España', 'rendimiento': 85},
    {'nombre': 'Maria', 'edad': 28, 'pais': 'Francia', 'rendimiento': 90},
    {'nombre': 'Pedro', 'edad': 30, 'pais': 'Italia', 'rendimiento': 85},
    {'nombre': 'Laura', 'edad': 27, 'pais': 'Italia', 'rendimiento': 85},
    {'nombre': 'Carlos', 'edad': 32, 'pais': 'Alemania', 'rendimiento': 80},
    {'nombre': 'Elena', 'edad': 29, 'pais': 'Alemania', 'rendimiento': 80}
] 
#mostrar los empleados ordenados por pais
mostrar_empleados_ordenados(empleados)  



