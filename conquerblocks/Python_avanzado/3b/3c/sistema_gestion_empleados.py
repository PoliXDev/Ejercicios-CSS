"""Crea un sistema de clases que maneje la información de 
los empleados, incluyendo empleados a tiempo completo y empleados a 
tiempo parcial.
- Clase base: `Empleado`
 - Atributos: nombre, apellido, salario base
- Clase derivada: `EmpleadoTiempoCompleto` (hereda de `Empleado`)
 - Atributo adicional: bono anual
- Clase derivada: `EmpleadoTiempoParcial` (hereda de `Empleado`)
 - Atributo adicional: horas trabajadas por semana
 Resuelve el problema creando instancias de estas clases y calculando los 
salarios totales para diferentes tipos de empleados"""

#clase base
class Empleado:
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base
    
    #metodo para calcular el salario mensual
    def calcular_salario_mensual(self):
        return self.salario_base / 12
    
    #metodo para mostrar informacion
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Salario base: {self.salario_base}"
    
    def calcular_salario_anual(self):
        return self.salario_base

#clase derivada
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, apellido, salario_base, bono_anual):
        super().__init__(nombre, apellido, salario_base)
        self.bono_anual = bono_anual
    
    def calcular_salario_mensual(self):
        salario_base_mensual = super().calcular_salario_mensual()
        bono_mensual = self.bono_anual / 12
        return salario_base_mensual + bono_mensual
    
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Bono anual: {self.bono_anual}"
    
    def calcular_salario_anual(self):
        return self.salario_base + self.bono_anual

#clase derivada (empleado tiempo parcial)
class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, apellido, salario_base, horas_trabajadas_semana):
        super().__init__(nombre, apellido, salario_base)
        self.horas_trabajadas_semana = horas_trabajadas_semana
    
    def calcular_salario_mensual(self):
        tarifa_hora = (self.salario_base / 52) / 40  # Salario por hora basado en 40 horas semanales
        return (tarifa_hora * self.horas_trabajadas_semana * 4)  # 4 semanas por mes
    
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Horas por semana: {self.horas_trabajadas_semana}"
    
    def calcular_salario_anual(self):
        tarifa_hora = (self.salario_base / 52) / 40
        return tarifa_hora * self.horas_trabajadas_semana * 52  # 52 semanas al año

#instancia de empleado tiempo completo
empleado_tiempo_completo = EmpleadoTiempoCompleto("Daniel", "Ruiz", 50000, 3000)

#instancia de empleado tiempo parcial
empleado_tiempo_parcial = EmpleadoTiempoParcial("Jessica", "Rodriguez", 30000, 25)

#mostrar informacion de los empleados
print(empleado_tiempo_completo.mostrar_informacion())
print(empleado_tiempo_parcial.mostrar_informacion())

#calcular salario mensual de los empleados (tiempo completo y tiempo parcial) con el formato de moneda
print(f"Salario mensual de {empleado_tiempo_completo.nombre} {empleado_tiempo_completo.apellido}: ${empleado_tiempo_completo.calcular_salario_mensual():,.2f}")
print(f"Salario mensual de {empleado_tiempo_parcial.nombre} {empleado_tiempo_parcial.apellido}: ${empleado_tiempo_parcial.calcular_salario_mensual():,.2f}")   

#calcular salario anual de los empleados (tiempo completo y tiempo parcial) con el formato de moneda
print(f"Salario anual de {empleado_tiempo_completo.nombre} {empleado_tiempo_completo.apellido}: ${empleado_tiempo_completo.calcular_salario_anual():,.2f}")
print(f"Salario anual de {empleado_tiempo_parcial.nombre} {empleado_tiempo_parcial.apellido}: ${empleado_tiempo_parcial.calcular_salario_anual():,.2f}")
    