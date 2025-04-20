#creamos la funcion generar_contrasena
import random
import string

def generar_contrasena(longitud, mayusculas, minusculas, numeros, caracteres_especiales):
    caracteres = ""

    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if caracteres_especiales:
        caracteres += string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(longitud))



