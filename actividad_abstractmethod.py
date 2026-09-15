# ACTIVIDAD - @abstractmethod
# Tema: Empleados y cálculo de salario

from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_bono(self):
        pass

    @abstractmethod
    def calcular_descuento(self):
        pass

    def calcular_salario_final(self):
        return self.salario_base + self.calcular_bono() - self.calcular_descuento()

    def mostrar_resumen(self):
        print(f"{self.nombre} ({type(self).__name__}) -> salario final: ${self.calcular_salario_final():,.0f}")


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, años_antiguedad):
        super().__init__(nombre, salario_base)
        self.años_antiguedad = años_antiguedad

    def calcular_bono(self):
        return self.salario_base * 0.05 * self.años_antiguedad

    def calcular_descuento(self):
        return self.salario_base * 0.08


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, valor_hora, horas_trabajadas):
        super().__init__(nombre, valor_hora * horas_trabajadas)
        self.horas_trabajadas = horas_trabajadas

    def calcular_bono(self):
        horas_extra = max(0, self.horas_trabajadas - 160)
        return horas_extra * 5000

    def calcular_descuento(self):
        return 0


class Gerente(EmpleadoTiempoCompleto):
    def __init__(self, nombre, salario_base, años_antiguedad, tamaño_equipo):
        super().__init__(nombre, salario_base, años_antiguedad)
        self.tamaño_equipo = tamaño_equipo

    def calcular_bono(self):
        bono_base = super().calcular_bono()
        return bono_base + (self.tamaño_equipo * 20000)


empleados = [
    EmpleadoTiempoCompleto("Carlos", 2_500_000, 3),
    EmpleadoPorHoras("Marta", 15_000, 180),
    Gerente("Laura", 4_000_000, 5, 8),
]

for e in empleados:
    e.mostrar_resumen()

total_nomina = sum(e.calcular_salario_final() for e in empleados)
print(f"\nTotal nómina: ${total_nomina:,.0f}")

# empleado_generico = Empleado("X", 1000)  # TypeError: no se puede instanciar
