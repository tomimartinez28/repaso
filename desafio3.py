"""
Desafío 3
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena. 

"""

def separar(lista):
    lista1 = []
    lista2 = []
    for numero in lista:
        if numero > 100:
            lista1.append(numero)
        else:
            lista2.append(numero)
    
    lista1.sort()
    lista2.sort()
    return lista1, lista2

lista = [5,5,6,4,8,5,2,7,2,5,5,58,5,25,569,150,220,300,125]

resul1 = separar(lista)[0]
resul2 = separar(lista)[1]

print(f"La primer lista es: {resul1} ")
print(f"La segunda lista es: {resul2} ")

