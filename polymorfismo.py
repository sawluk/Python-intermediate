# DIFERENTES TIPOS DE VALORES QUE SE LE PUEDE DAR A UNA VARIABLES

x = 20
y = 15.5
z = x + y
print(z)
x = "luis"
print(x)

# Segundo tipo de polimorfismo

lista1 = [1, 2, 3, 4, 5]
lista2 = ['jorge', 'noguera', 'pelo rosado', 'Samulx', 'yo']

def recorrer_lista(lista):
    for elemento in lista:
        print(elemento)

recorrer_lista(lista1)
recorrer_lista(lista2)


# Tercer tipo, cuando hay clases con un metodo de un mismo nombre
# la respuesta seguira siendo diferente
# Funcion a la que envio un parametro de las clases anteriores y 
# que en respuesta me de el sonido correspondiente

def sonido_animal(animal):
    animal.sonido()

class Gato():
    def sonido(self):
        print("Miau");

class Perro():
    def sonido(self):
        print("Guau");

g1 = Gato()
sonido_animal(g1)

p1 = Perro()
sonido_animal(p1)

# Mismo nombre en circunstancias diferentes