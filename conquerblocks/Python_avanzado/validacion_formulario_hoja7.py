#Crea un programa que valide un formulario de registro. Crea una función 
#llamada validar_formulario que reciba diferentes campos de un formulario 
#(nombre, correo electrónico y número de teléfono) y verifique si los valores 
#ingresados cumplen con los requisitos especificados, siendo estos:
#1. Que el nombre tenga una longitud minima de 3 caracteres
#2. Que el teléfono este conformado por dígitos y tenga una longitud de 9 
#caracteres
#3. Que el email contenga un “@“ y un “.

def validar_formulario(nombre, telefono, email):
    if len(nombre) < 3:
        return False,"El nombre debe tener una longitud mínima de 3 caracteres"
    if not telefono.isdigit() or len(telefono) != 9:
        return False, "El teléfono debe estar conformado por 9 dígitos"
    if "@" not in email or "." not in email:
        return False, "El email debe contener un '@' y un '.'"
    return True, "Formulario válido"

nombre = input("Ingrese su nombre: ")
telefono = input("Ingrese su teléfono: ")
email = input("Ingrese su email: ")

es_valido, mensaje = validar_formulario(nombre, telefono, email)
print(mensaje)

