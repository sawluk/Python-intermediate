# Ejemplo basico de decoradores en python

# Ejemplo
def Decorador(d1):
    def DecoradorInterno():
        print("Persona en proceso de registro")
        d1()
        print("Registrado\n")
    return DecoradorInterno()

@Decorador
def Person1():
    print("Hola mi nombre es Noguera")  
    
@Decorador
def Person2():
    print("Hola mi nombre es Bolaños")  


