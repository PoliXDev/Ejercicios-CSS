#escribe un programa que lea el archivo novela_ejercicio.txt y cuente cuantas veces aparece cada palabra en el archivo.
#pide al usuario que ingrese una palabra y muestra cuantas veces aparece en el archivo.

ruta_base = "/home/noahknox/Documents/conquerblocks/python_avanzado/manipulacion_archivos_hoja2_python_avanzado/"

palabra = input("Ingrese una palabra: ")

def contar_palabra(palabra):
    with open(ruta_base + "novela_ejercicio.txt", "r") as archivo:
        contenido = archivo.read()
        return contenido.count(palabra)

print("La palabra", palabra, "aparece", contar_palabra(palabra), "veces en el archivo.")



