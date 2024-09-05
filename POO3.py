# Erencia en Python 

class Persona:
    def __init__(self, nombre, edad, direccion, correo):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.correo = correo

    def caminar(self):
        print(self.nombre + " está caminando.")

    def correr(self):
        print(self.nombre + " está corriendo.")

    def comer(self):
        print(self.nombre + " está comiendo.")


class Estudiante(Persona):
    def __init__(self, nombre, edad, direccion, correo, semestre, nota):
        super().__init__(nombre, edad, direccion, correo)
        self.semestre = semestre
        self.nota = nota

    def ganar_semestre(self):
        print(self.nombre + " ha ganado el semestre de python")

    def perder_semestre(self):
        print(self.nombre + " ha perdido el semestre de python")


class Profesor(Persona):
    def __init__(self, nombre, edad, direccion, correo, salario):
        super().__init__(nombre, edad, direccion, correo)

        self.salario = salario

    def dictar_clase(self):
        print(self.nombre + " esta dictando clase")

    def evaluar(self):
        print(self.nombre + " está evaluando.")
