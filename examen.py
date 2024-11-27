import math

# Clase base Figura
class Figura:
    def area(self):
        return 0

# Clase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Clase Círculo que hereda de Figura
class Círculo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

# Creación de instancias
c = Cuadrado(4)
clo = Círculo(3)
cdo = Cuadrado(5)

# Mostrar el área de ambas figuras
print(f"El área del cuadrado es: {c.area()}")
print(f"El área del círculo es: {clo.area()}")
print(f"El área del cuadrado 2 es: {cdo.area()}")