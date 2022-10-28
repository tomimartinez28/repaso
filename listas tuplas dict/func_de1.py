"""
Ejercicio 2: Tarifa del taxi

En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, más $15.00 por cada 140 metros recorridos. Escriba una función que tome la distancia recorrida (en kilómetros) como su único parámetro y devuelva la tarifa total como su único resultado. Escriba un programa principal que use la función.

Sugerencia: Utilice constantes para presentar la base y la porción variable de las tarifas así el programa podrá actualizar fácilmente cuando las tasas aumentan.

"""

BASE = 40
PORCION_VARIABLE = (15/0.14)


def tarifa(kms):
    return BASE + kms * PORCION_VARIABLE


distancia = float(input("Indique cuantos kms recorrio: >> "))

resultado = tarifa(distancia)
print(f"La tarifa total es {round(resultado,2)} pesos.")


round()
