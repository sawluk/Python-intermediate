class Estudiante:
    def __init__(self, nombre, edad, semestre, nota):
        self.nombre = nombre
        self.edad = edad
        self.semestre = semestre
        self.nota = nota

    def ganar_semestre(self):
        print(self.nombre + " ha ganado el semestre de python")

    def perder_semestre(self):
        print(self.nombre + " ha perdido el semestre de python")
       

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
semestre = int(input("Ingrese el semestre del estudiante: "))
nota = float(input("Ingrese la nota del estudiante: "))

estudiante = Estudiante(nombre, edad, semestre, nota)

if estudiante.nota >= 3.5:
    estudiante.ganar_semestre()
else:
    estudiante.perder_semestre()