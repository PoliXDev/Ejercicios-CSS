#Crea un sistema de gestión de una biblioteca utilizando clases en Python. 
#Debes implementar las siguientes clases:

#1. “Libro”: Representa un libro con atributos como título, autor y número de 
#ejemplares disponibles.

#2. “Usuario”: Representa a un usuario de la biblioteca con atributos como 
#nombre, número de identificación y lista de libros prestados.

#3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar 
#libros, prestar libros a usuarios, devolver libros y mostrar el inventario

#clase libro
class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares    

#clase usuario
class Usuario:
    def __init__(self, nombre, id, libros_prestados):
        self.nombre = nombre
        self.id = id
        self.libros_prestados = libros_prestados

#clase biblioteca
class Biblioteca:
    def __init__(self, libros, usuarios):
        self.libros = libros
        self.usuarios = usuarios
# metodo para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

# metodo para prestar un libro a un usuario
    def prestar_libro(self, usuario, libro):
        if libro in self.libros and libro not in usuario.libros_prestados:
            usuario.libros_prestados.append(libro)
            self.libros.remove(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print(f"Libro '{libro.titulo}' no disponible para prestar.")

# metodo para devolver un libro a la biblioteca
    def devolver_libro(self, usuario, libro):
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            self.libros.append(libro)
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")

# metodo para mostrar el inventario de la biblioteca
    def mostrar_inventario(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Inventario de la biblioteca:")
            for libro in self.libros:
                print(f"- {libro.titulo} por {libro.autor} ({libro.ejemplares} ejemplares)")

#ejemplo de uso
pablo = Usuario("Daniel", 123456789, [])
biblioteca = Biblioteca([], [pablo])

libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 10)
libro2 = Libro("1984", "George Orwell", 5)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)    

biblioteca.mostrar_inventario()

biblioteca.prestar_libro(pablo, libro1)
biblioteca.mostrar_inventario()

biblioteca.devolver_libro(pablo, libro1)
biblioteca.mostrar_inventario() 


