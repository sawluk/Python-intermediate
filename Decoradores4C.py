def decorador(fichero):
    def decorador_N(func):
        def wrapper(*args, **kwargs):
            print("Los resultados son: ")
            with open(fichero, "a") as abrir:
                output = func(*args, **kwargs)
                abrir.write(f"{output}\n")
                print(f"Resultado: {output}")  # Muestra el resultado también en consola
                print("-------------------------")
            return output  # Devuelve el resultado de la función
        return wrapper
    return decorador_N

@decorador('ficherossalida.log')
def suma(a, b):
    print("Suma")
    return a + b

@decorador('ficherossalida.log')
def resta(c, d):
    print("Resta")
    return c - d

@decorador('ficherossalida.log')
def multi(f, g):
    print("Multiplicación")
    return f * g

@decorador('ficherossalida.log')
def division(h, i):
    print("División")
    return h / i

@decorador('ficherossalida.log')
def todo(o, p, q, r):
    print("Mezcla")
    return (((o + p) - q) / r) * o

@decorador('ficherossalida.log')
def areaTriangulo(j, k):
    print("Área Triángulo")
    return (j * k) / 2

# Llamadas a las funciones
suma(5, 5)
resta(6, 2)
multi(5, 4)
division(10, 2)
todo(20, 10, 5, 6)
areaTriangulo(3, 4)
