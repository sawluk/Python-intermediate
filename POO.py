class Vehiculo:
    def __init__(self, marca, ref, mod):
        self.marca = marca
        self.ref = ref
        self.mod = mod
    
    def arrancar(self):
        print("El vehiculo arranco y su marca es " + self.marca + " de modelo " + self.mod)

vehiculo1 = Vehiculo("Toyota", "Corolla", "2023")
vehiculo2 = Vehiculo("Ford", "Mustang", "2000")
vehiculo3 = Vehiculo("Honda", "Civic", "2021")

print(vehiculo1.mod)
print(vehiculo2.ref)
print(vehiculo3.marca)

vehiculo1.arrancar()
vehiculo2.arrancar()
vehiculo3.arrancar()



