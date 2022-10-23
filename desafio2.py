from desafio3 import imprimir_numeros
"""
Desafío 2
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.

Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas.

"""

def relacion(a, b):
    if a > b:
        return nombre_ciudad1
    elif b > a:
        return nombre_ciudad2
    else:
        return nombre_ciudad1, nombre_ciudad2

nombre_ciudad1 = input("Ingrese el nombre de la primer ciudad: ")
tonelada_ciudad1 = float(input(f"Ingrese la cantidad de toneladas recicladas en {nombre_ciudad1}: "))

nombre_ciudad2 = input("Ingrese el nombre de la segunda ciudad: ")
tonelada_ciudad2 = float(input(f"Ingrese la cantidad de toneladas recicladas en {nombre_ciudad2}: "))


resul = relacion(tonelada_ciudad1, tonelada_ciudad2)


print(f"La ciudad es:{resul} ")
