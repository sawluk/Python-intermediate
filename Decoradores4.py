def decorador(fichero):
    def decorador_N(func):
        def wrapper(*args, **kwargs):
            print("Los resultados son: ")
            with open(fichero, "a") as abrir:
                output = func(*args, **kwargs)
                abrir.write(f"{output}\n")
                print("-------------------------")
        return wrapper
    return decorador_N

@decorador('ficherossalida.log')
def suma(a,b):
    print("Suma")
    return print (a + b)

@decorador('ficherossalida.log')
def resta(c,d):
    print("Resta")
    return print (c - d)

@decorador('ficherossalida.log')
def multi(f,g):
    print("Multiplicacion")
    return print (f * g)

@decorador('ficherossalida.log')
def division(h,i):
    print("Division")
    return print (h / i)

@decorador('ficherossalida.log')
def todo(o,p,q,r):
    print("Mezcla")
    return print ((((o+p)-q)/r) * o)

@decorador('ficherossalida.log')
def areaTrinagulo(j,k):
    print("Area Triangulo")
    return print((j * k) / 2)


suma(5,5)
resta(6,2)
multi(5,4)
division(10,2)
todo(20,10,5,6)
areaTrinagulo(3,4)