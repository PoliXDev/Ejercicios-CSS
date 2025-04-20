#creamos la funcion validar_contrasena
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    return True 

