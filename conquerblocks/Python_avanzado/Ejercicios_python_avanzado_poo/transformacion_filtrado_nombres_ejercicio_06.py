"""desarrolla una herramienta de procesamiento de nombres para una aplicación de gestión de contactos. 
tienes una lista de nombres con el formato "Apellido, Nombre", realiza las siguientes tareas:
1. Utiliza la función lambda para transformar una lista de nombres completos
al nuevo formato.
2. Filtra la lista para incluir solo los nombres que contienen al menos dos
vocales y tienen una longitud mayor a 10 caracteres."""

import re

lista_nombres = ["García, Juan", "Pérez, María", "López, Ana", "Gómez, Luis", "Rodríguez, Laura"]

# 1. Utiliza la función lambda para transformar una lista de nombres completos al nuevo formato.
lista_nombres_transformada = list(map(lambda nombre: nombre.split(",")[1].strip() + " " + nombre.split(",")[0].strip(), lista_nombres))
print("Lista de nombres transformada:")
for nombre in lista_nombres_transformada:
    print(f"- {nombre}")

print("\n") # Separador para mejor legibilidad

# 2. Filtra la lista para incluir solo los nombres que contienen al menos dos vocales y tienen una longitud mayor a 10 caracteres.
lista_nombres_filtrada = list(filter(lambda nombre: len(nombre) > 10 and len(re.findall(r'[aeiouAEIOU]', nombre)) >= 2, lista_nombres_transformada))
print("Lista de nombres filtrada (>10 caracteres y ≥2 vocales):")
for nombre in lista_nombres_filtrada:
    print(f"- {nombre}")



