"""estoy trabajando en el desarrollo de un sistema para una
aplicación de gestión de documentos en un entorno empresarial. Deseo
implementar un decorador llamado verificar_acceso_entorno que permita
controlar el acceso a funciones según el entorno de ejecución.
El decorador debe realizar las siguientes acciones:
1. Antes de ejecutar la función, verificar si el entorno de ejecución es
"producción".
2. Si el entorno es "producción", permitir la ejecución de la función y mostrar
un mensaje indicando que el acceso fue permitido en el entorno de
producción.
3. Si el entorno no es "producción", evitar la ejecución de la función y mostrar
un mensaje indicando que el acceso está restringido a entornos de
producción.
Luego, aplica este decorador a dos funciones, " subir_documento" y 
"eliminar_documento"."""

#menu para elegir el entorno de ejecucion
def menu():
    print("\n=== SELECCIÓN DE ENTORNO ===")
    print("1. Producción")
    print("2. Desarrollo")
    
    while True:
        try:
            opcion = int(input("Seleccione el entorno (1-2): "))
            if opcion == 1:
                return "producción"
            elif opcion == 2:
                return "desarrollo"
            else:
                print("Error: Por favor seleccione 1 o 2")
        except ValueError:
            print("Error: Por favor ingrese un número válido")

#decorador para verificar el acceso al entorno
def verificar_acceso_entorno(func):
    def wrapper(*args, **kwargs):
        entorno = menu()
        print(f"\nEntorno seleccionado: {entorno}")
        if entorno.lower() == "producción":
            print("✅ Acceso permitido en entorno de producción")
            return func(*args, **kwargs)
        else:
            print("❌ Acceso restringido. Solo se permite en entorno de producción")
            return None
    return wrapper

#funcion subir_documento
@verificar_acceso_entorno
def subir_documento():
    print("📤 Subiendo documento...")

#funcion eliminar_documento
@verificar_acceso_entorno
def eliminar_documento():
    print("🗑️ Eliminando documento...")

#menu principal
if __name__ == "__main__":
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Subir documento")
        print("2. Eliminar documento")
        print("3. Salir")
        
        try:
            opcion = int(input("Seleccione una opción (1-3): "))
            if opcion == 1:
                subir_documento()
            elif opcion == 2:
                eliminar_documento()
            elif opcion == 3:
                print("¡Programa finalizado!")
                break
            else:
                print("Error: Por favor seleccione una opción válida (1-3)")
        except ValueError:
            print("Error: Por favor ingrese un número válido")

menu()  