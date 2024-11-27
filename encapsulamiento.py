# El encapsulamiento se refiere a darle seguirdad dentro de lo que se presenta
# Se pueden encapsular metodos, o atributos, en python es mediante dos guiones hacia abajo  .__
#Para poder acceder a un metodo privado, se debe realizar getters y setters

class Persona():
    def __init__(self, nombre, id):
        self.nombre = nombre  
        self.__id = id
    
    def __hablarpriv(self):
        print("Hola, soy " + self.nombre)

    def hola(self):
        print("hola")
    
    def get_id(self):
        return self.__id 
    
    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

# metodo publico para acceder al privado
    def hablar_publico(self):
        self.__hablarpriv()
        

pedro = Persona("Pepe", 123)

print(pedro.get_nombre())
print(pedro.get_id())
pedro.hablar_publico()
pedro.hola()











