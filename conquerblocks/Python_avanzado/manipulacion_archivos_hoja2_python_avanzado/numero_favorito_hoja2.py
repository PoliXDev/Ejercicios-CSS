#pedir numero favorito.
#guardar numero favorito en archivo json.
#comproba si tenemos el numero favorito.
#imprimir el numero favorito.   

import json

def comprobar_numero_favorito():
    try:
        with open("numero_favorito.json", "r") as archivo:
            contenido = archivo.read()
            if not contenido:  # Si el archivo está vacío
                return None
            num_favorito = json.loads(contenido)
        return num_favorito
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    
def guardar_numero_favorito(numero):
    with open("numero_favorito.json", "w") as archivo:
        json.dump(numero, archivo)

def preguntar_numero_favorito():
    try:
        num_favorito = int(input("Introduce tu número favorito: "))
        guardar_numero_favorito(num_favorito)
        print("El número favorito se ha guardado")
        return num_favorito
    except ValueError:
        print("Error: Por favor, introduce un número válido")
        return None

def imprimir_numero_favorito():
    num_favorito = comprobar_numero_favorito()
    if num_favorito:
        print(f"El número favorito es: {num_favorito}")
    else:
        print("No hay un número favorito guardado")

#programa principal
if __name__ == "__main__":
    while True:
        num_favorito = comprobar_numero_favorito()
        if num_favorito:
            imprimir_numero_favorito()
            break
        else:
            if preguntar_numero_favorito() is not None:
                break
            # Si preguntar_numero_favorito retorna None, el bucle continuará
    