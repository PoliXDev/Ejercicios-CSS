#has una funcion que pida al usuario busque una fecha de nacimiento en el archivo pi_10000.txt
#y devuelva la fecha de nacimiento y la cantidad de veces que aparece en el archivo.

ruta_base = "/home/noahknox/Documents/conquerblocks/python_avanzado/manipulacion_archivos_hoja2_python_avanzado/"

fecha = input("Ingrese una fecha de nacimiento: ")

def buscar_fecha(fecha):
    with open(ruta_base + "pi_10000.txt", "r") as archivo:
        contenido = archivo.read()
        return contenido.count(fecha)

print("La fecha", fecha, "aparece", buscar_fecha(fecha), "veces en el archivo.")

