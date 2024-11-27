def mi_decorador(func):
    def envoltura():
        print("Estamos envoltura de mi decorador")
        func()
        print("Saliendo del decorador")
    return envoltura

@mi_decorador
def saludo():
    print("Hola, esto es un mensaje decorado")

saludo()

print("--------------------------------\n")