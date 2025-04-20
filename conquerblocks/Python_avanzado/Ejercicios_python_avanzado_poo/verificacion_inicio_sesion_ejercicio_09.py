"""Estoy desarrollando un sistema de autenticación para una aplicación web y
deseo implementar un sistema de inicio de sesión que verifique si las
credenciales proporcionadas por el usuario son válidas antes de permitir el
acceso a ciertas funciones. Además, deseas que una vez que el usuario haya
iniciado sesión correctamente, se le proporcione información personal.
Implementa lo siguiente:

1. Un registro de usuarios que contenga información adicional, como el
nombre completo y el correo electrónico.

2. Un decorador llamado verificar_inicio_sesion que acepte el nombre de
usuario y la contraseña como argumentos. Este decorador verificará si las
credenciales proporcionadas son válidas comparándolas con el registro de
usuarios. Si las credenciales son válidas, la función decorada se ejecutará y
se le pasará como argumento la información personal del usuario.

3. Una función llamada informacion_usuario que imprima la información personal
del usuario después de que haya iniciado sesión correctamente.
Implementa este sistema de inicio de sesión utilizando decoradores."""

# Registro de usuarios
usuarios = {
    "jpro": {
        "contraseña": "123456", 
        "nombre": "Juan Pérez Rodriguez", 
        "correo": "juan.perez@gmail.com"
    },
    "mgomez22": {
        "contraseña": "222222", 
        "nombre": "María Gómez Sánchez", 
        "correo": "maria.gomez@gmail.com"
    },
    "carlitos_l": {
        "contraseña": "111111", 
        "nombre": "Carlos López Martinez", 
        "correo": "carlos.lopez@gmail.com"
    }
}   
#menu de inicio
def menu():
    while True:
        print("\n=== SISTEMA DE INICIO DE SESIÓN ===")
        print("Nicknames disponibles para pruebas: jpro, mgomez22, carlitos_l")
        print("1. Iniciar sesión")
        print("2. Salir")
        try:
            opcion = int(input("Seleccione una opción (1-2): "))
            if opcion in [1, 2]:
                return opcion
            print("❌ Por favor, seleccione una opción válida (1-2)")
        except ValueError:
            print("❌ Por favor, ingrese un número válido")

#decorador para verificar el inicio de sesion
def verificar_inicio_sesion(func):
    def wrapper():
        intentos = 0
        while intentos < 2:
            nickname = input("Ingrese su nickname: ")
            contraseña = input("Ingrese su contraseña: ")
            
            if nickname in usuarios and usuarios[nickname]["contraseña"] == contraseña:
                return func(usuarios[nickname])
            else:
                intentos += 1
                intentos_restantes = 2 - intentos
                print(f"❌ Credenciales inválidas. Le quedan {intentos_restantes} intentos")
        
        print("❌ Ha excedido el número máximo de intentos")
        return None
    return wrapper

#funcion para imprimir la informacion del usuario
@verificar_inicio_sesion
def informacion_usuario(usuario):
    print("\n=== INFORMACIÓN DEL USUARIO ===")
    print(f"👤 Nombre completo: {usuario['nombre']}")
    print(f"📧 Correo electrónico: {usuario['correo']}")
    return True

#funcion principal
def main():
    while True:
        opcion = menu()
        if opcion == 1:
            if informacion_usuario() is None:  
                continue
        else:
            print("¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()

