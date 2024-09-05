class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def caminar(self):
        print(self.nombre + " está caminando.")

    def correr(self):
        print(self.nombre + " está corriendo.")

    def comer(self):
        print(self.nombre + " está comiendo.")

class Profesional(Persona):
    def __init__(self, nombre, edad, salario, titulo):
        super().__init__(nombre, edad)
        self.titulo = titulo
        self.salario = salario

    def dictar_clase(self):
        print(self.nombre + " está dictando clase.")

    def evaluar(self):
        print(self.nombre + " está evaluando.")

class Empleado(Profesional): 
    def __init__(self, nombre, edad, salario, titulo, cargo):
        super().__init__(nombre, edad, salario, titulo)  
        self.cargo = cargo

    def laburando(self):
        print(self.nombre + " tiene un titulo de: " + self.titulo + " y trabaja como " + self.cargo + " ganando " + str(self.salario))

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
salario = int(input("Ingrese el salario: "))
titulo = input("Ingrese el título: ")
cargo = input("Ingrese el cargo: ")

Coso = Empleado(nombre, edad, salario, titulo, cargo)
Coso.laburando()
Coso.comer()


