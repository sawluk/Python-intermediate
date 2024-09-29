# David Noguera, Samuel Bolaños (Apoyo emocional Monitor: Miguel Montufar)

def hacer_hablar(animal):
    animal.hablar()

class Animal():
    def __init__(self, nombre, edad):
        self.__nombre = nombre  
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return str(self.__edad)

    def set_edad(self, edad):
        self.__edad = edad

    def describir(self):
        return (f"se llama {self.__nombre} y tiene {self.__edad} años.")

    def hablar(self):
        print("")

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hablar(self):
        print("Guuuuaa")

    def describir(self):
        return "Este es un perro " + super().describir()

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hablar(self):
        print("Miami")

    def describir(self):
        return "Este es un gato " + super().describir()

class Pajaro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hablar(self):
        print("Pio pio")

    def describir(self):
        return "Este es un pájaro " + super().describir()



pajaro = Pajaro("Pepe", 3)
print(pajaro.get_nombre())
print(pajaro.get_edad())
hacer_hablar(pajaro)

#-------------------------------------
g1 = Gato("", 0)
nombre = input("Dale un nombre al gato: ")
g1.set_nombre(nombre)
edad = input("Cual es la edad del gato: ")
g1.set_edad(edad)
hacer_hablar(g1)
print(g1.describir())
print(g1.get_nombre())
print(g1.get_edad())

#-------------------------------------
labrador = Perro("", 0)
nombre = input("Dale un nombre al perro: ")
labrador.set_nombre(nombre)
edad = input("Cual es la edad del perro: ")
labrador.set_edad(edad)
hacer_hablar(labrador)
print(labrador.describir())

#-------------------------------------

