"""
Desafío 1

150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 

Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.

"""

"""
LISTA_ELEMENTOS = ["bolsa de plastico", "botella de pet", "envases de tetrabrik", "chicle"]

def tiempo_degradado(elemento):
    if elemento == "bolsa de plastico":
        return 150
    elif elemento == "botella de pet":
        return 1000
    elif elemento == "envases de tetrabrik":
        return 30
    elif elemento == "chicle":
        return 5
    

eleccion = input("Elegir uno de los siguientes elementos\n1-Bolsa de Plastico \n2-Botella de PET \n3-Envase de Tetrabrik \n4-Chicle \n >>").lower()



if eleccion not in LISTA_ELEMENTOS:
    print("Opcion incorrecta")
else:
    resul = tiempo_degradado(eleccion)
    print(f" {resul} años")

"""






## VERSION MAS COMPLEJA

LISTA_ELEMENTOS = [
    {"cod" : "1" , "elemento" : "Bolsa de Plastico","años" : 150},

    {"cod" : "2" , "elemento" : "Botella PET","años" : 150},

    {"cod" : "3" , "elemento" : "Envase de Tetrabrik","años" : 150},

    {"cod" : "4" , "elemento" : "Chicle","años" : 150},

    {"cod" : "5" , "elemento" : "Vidrio", "años" : 10000},


]

def mostrar_elementos():
    print("===========================================")
    for ele in LISTA_ELEMENTOS:
        print(f" {ele['cod']} - {ele['elemento']}")
    print("===========================================")


def tiempo_degradado(opcion):
    for ele in LISTA_ELEMENTOS:
        if opcion == ele['cod']:
            return ele['años']



print("Bienvenido. Indique un elemento de la lista, para conocer cuanto tarda:")
mostrar_elementos()
opcion = input(">> ")

resul = tiempo_degradado(opcion)
print(f"El elemento elegido tarda {resul} años. ")
