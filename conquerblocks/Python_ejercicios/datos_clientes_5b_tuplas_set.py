#Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene
#el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La
#segunda base de datos contiene el nombre del cliente, la dirección y el historial de
#pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y
#devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en
#ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre

base_datos1 = [("Juan", "juan@example.com", "555-1234"),
               ("Maria", "maria@example.com", "555-5678"),
               ("Pedro", "pedro@example.com", "555-9012")
]

base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]),
            ("Maria", "Calle 456", ["Libro3"]),
            ("Luis", "Calle 789", ["Libro4"])
]

# Crear un conjunto para almacenar los nombres de los clientes en la primera base de datos
clientes_base_datos1 = {cliente[0] for cliente in base_datos1}

# Crear un conjunto para almacenar los nombres de los clientes en la segunda base de datos
clientes_base_datos2 = {cliente[0] for cliente in base_datos2}

# Encontrar los clientes que aparecen en ambas bases de datos
clientes_en_ambas_bases = clientes_base_datos1.intersection(clientes_base_datos2)

# Filtrar las tuplas de ambas bases de datos para incluir solo los clientes que aparecen en ambas
base_datos_combinada = [(cliente, base_datos1[i][1], base_datos1[i][2])
                         for i, cliente in enumerate(base_datos1)
                         if cliente[0] in clientes_en_ambas_bases]

#imprimir un nueva lista de tuplas que contenga solo los clientes que aparecen en ambas bases de datos
print(base_datos_combinada)
