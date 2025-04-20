import os

# Definir la ruta base donde se encuentran los archivos
ruta_base = "/home/noahknox/Documents/conquerblocks/python_avanzado/manipulacion_archivos_hoja2_python_avanzado/"

def leer_archivos(archivo1, archivo2):
    for nombre_archivo in (archivo1, archivo2):
        ruta_completa = os.path.join(ruta_base, nombre_archivo)
        try:
            with open(ruta_completa, 'r') as f:
                contenido = f.read()
                print(f"Contenido de {nombre_archivo}:")
                print(contenido)
                print()  # Línea en blanco entre archivos
        except FileNotFoundError:
            pass

leer_archivos('cats.txt', 'dogs.txt')
print("fin")
