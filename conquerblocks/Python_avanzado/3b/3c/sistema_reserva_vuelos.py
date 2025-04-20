"""Crea un sistema de clases que permita a los usuarios realizar 
#reservas de vuelos. Aquí tienes una posible estructura:
#- Clase base: `Vuelo`
# - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de 
pasajeros
 - Métodos: agregar pasajero, verificar disponibilidad de asientos
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
 - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones, 
trabajo)
Resuelve el problema creando instancias de estas clases y realizando 
reservas para diferentes vuelos y tipos de vuelos especiales"""

#clase vuelo
class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, capacidad_maxima, lista_pasajeros):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad_maxima = capacidad_maxima
        self.lista_pasajeros = lista_pasajeros

    # metodo para agregar pasajero
    def agregar_pasajero(self, pasajero):
        if len(self.lista_pasajeros) < self.capacidad_maxima:
            self.lista_pasajeros.append(pasajero)
            print(f"Pasajero {pasajero} agregado al vuelo {self.numero_vuelo}.")
        else:
            print(f"No hay asientos disponibles para el vuelo {self.numero_vuelo}.")
   
    #metodo para verificar disponibilidad de asientos
    def verificar_disponibilidad_asientos(self):
        asientos_disponibles = self.capacidad_maxima - len(self.lista_pasajeros)
        print(f"Asientos disponibles: {asientos_disponibles}")
        return len(self.lista_pasajeros) < self.capacidad_maxima

    #metodo para mostrar informacion
    def mostrar_informacion(self):
        print(f"Vuelo {self.numero_vuelo} - {self.origen} a {self.destino}")
        print(f"Capacidad máxima: {self.capacidad_maxima}")
        print(f"Pasajeros: {self.lista_pasajeros}")
        print(f"Asientos disponibles: {self.capacidad_maxima - len(self.lista_pasajeros)}")

#clase vuelo especial
class VueloEspecial(Vuelo):
    def __init__(self, numero_vuelo, origen, destino, capacidad_maxima, lista_pasajeros, motivo):
        super().__init__(numero_vuelo, origen, destino, capacidad_maxima, lista_pasajeros)
        self.motivo = motivo
    
    #metodo para mostrar informacion
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Motivo del vuelo especial: {self.motivo}")

#instancia de vuelo
vuelo1 = Vuelo(123, "Madrid", "Barcelona", 200, [])
vuelo2 = VueloEspecial(456, "Madrid", "Barcelona", 200, [], "Vacaciones")

#reserva de vuelo y vuelo especial y el motivo
vuelo1.agregar_pasajero("Juan")
vuelo1.mostrar_informacion()
vuelo2.agregar_pasajero("Maria")
vuelo2.mostrar_informacion()


