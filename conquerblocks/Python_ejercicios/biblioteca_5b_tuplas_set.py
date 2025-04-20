#Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista
#de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
#libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del libro y el apellido del autor.

lista_libros = [('El aleph', 'Jorge Luis Borges'), ('Cien años de soledad', 'Garbriel Garcia Márquez'), ('La ciudad y los perros', 'Mario Vargas Llosa')]

# paso 1: eliminar los libros duplicados

for libro, autor in lista_libros:
    libros_unicos = set(libro)


# paso 2: devolver una nueva lista de tuplas que contenga el título del libro y el apellido del autor.

def obtener_apellidos_autores(lista_libros):
    apellidos_autores = []
    for libro, autor in lista_libros:
        # El error está aquí. Algunos autores tienen más de dos nombres.
        apellido_autor = autor.split()[-1]
        apellidos_autores.append((libro, apellido_autor))
    return apellidos_autores  # Añadimos esta línea para devolver el resultado

resultado = obtener_apellidos_autores(lista_libros)
print(resultado)
