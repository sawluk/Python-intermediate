class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

    def comer(self):
        print("hola me llamo ", self.nombre, " y estoy comiendo")

class Jugador(Persona):
    def __init__(self, edad, nombre, equipo, posicion, salario):
        super().__init__(edad, nombre)
        self.equipo = equipo
        self.posicion = posicion
        self.salario = salario

    def jugar(self):
        print(f"hola me llamo {self.nombre} y estoy jugando y tengo {self.edad} años")

    def desayunar(self):
        super().comer()
        print("Estoy desayunando")

    def comer(self):
        return super().comer()


class Empleado(Jugador):
    def __init__(self, edad, nombre, equipo, posicion, sal):
        super().__init__(edad, nombre, equipo, posicion, sal)
        self.salario = sal

    def trabajar(self):
        print("estoy trabajando")

    def comer(self):
        return super().comer()

    def jugar(self):
        return super().jugar()


nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
equipo = input("Ingrese el equipo: ")
posicion = input("Ingrese la posicion: ")
sal = int(input("Ingrese su salario: "))

jug1 = Empleado(edad, nombre, equipo, posicion, sal)
jug2 = Jugador(35, "cristiano", "portugal", "delantero", 1000000)

jug1.comer()
jug1.jugar()
