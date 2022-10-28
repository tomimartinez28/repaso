"""

Desafío 1
Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10, almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. 
"""

lista = []
seguir = True


while seguir:
    conocimiento = input("Cuando conoces sobre contaminacion? >> ")
    lista.append(conocimiento)

    respuesta = input("Desea registrar una persona mas? \nsi/no >>")
    if respuesta == "no":
        seguir = False


lista.sort()


print(f"su lista es: {lista} ")


