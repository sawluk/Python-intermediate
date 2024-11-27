# Función para calcular la potencia de un número
def potencia(base, exponente):
    resultado = 1  # Comenzamos con 1 porque es el elemento neutro de la multiplicación
    
    if exponente > 0:
        while exponente > 0:
            resultado *= base  # Multiplicamos el resultado por la base
            exponente -= 1     # Reducimos el exponente en 1 en cada iteración
        return resultado
    elif exponente == 0:
        return 1
    else:
        return "El exponente no puede ser negativo"  # Manejo de exponentes negativos

# Prueba de la función
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es {resultado}")
