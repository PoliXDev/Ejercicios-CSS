#Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
#Crea un programa que tome una base de datos de una red social como una lista de
#tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. 
#Losnombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
#diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
#tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.

#Ejemplo:

#Base de datos de usuarios y sus amigos:

red_social = [("Juan", ["Maria", "Pedro", "Luis"]),
            ("Maria", ["Juan", "Pedro", "Juan"]),
            ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"]
            )]



#Explicación:
#El usuario "Juan" tiene 3 amigos: "Maria", "Pedro" y "Luis".
#El usuario "Maria" tiene 2 amigos: "Juan" y "Pedro".
#El usuario "Pedro" tiene 2 amigos: "Juan" y "Maria".
#El usuario "Luis" tiene 1 amigo: "Juan".

# paso 1: eliminar las cuentas duplicadas
# paso 2: devolver una tupla de tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.

# paso 1: eliminar las cuentas duplicadas

for usuario, amigos in red_social:
    amigos_unicos = set(amigos)
    print(amigos_unicos)

# paso 2: devolver una tupla de tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.

def obtener_estadisticas_amigos(red_social):
    estadisticas = []
    usuario_mas_amigos = None
    max_amigos = 0

    for usuario, amigos in red_social:
        num_amigos = len(set(amigos))
        estadisticas.append((usuario, num_amigos))
        
        if num_amigos > max_amigos:
            max_amigos = num_amigos
            usuario_mas_amigos = usuario

    return tuple(estadisticas), (max_amigos, usuario_mas_amigos)

resultado = obtener_estadisticas_amigos(red_social)
print(f"Estadísticas de amigos: {resultado[0]}")
print(f"Usuario con más amigos: {resultado[1]}")
