def decorador_con_mensaje(mensaje):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(f"{mensaje}")
            result = func(*args, **kwargs)
            print("------------------------")
            return result
        return wrapper  # Se devuelve el wrapper aquí
    return decorador  # Se devuelve el decorador aquí

@decorador_con_mensaje("Ejecutando la función")
def mi_funcion(x, y):
    return x + y

resultado = mi_funcion(5, 3)
print("Resultado:", resultado)