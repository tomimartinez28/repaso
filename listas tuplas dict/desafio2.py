"""
Desafío 2	
Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.

El programa termina cuando el usuario introduce un cero.
"""

factores = ("Las Aguas Residuales","Las Sustancias Químicas Tóxicas",
"Las Aguas Pluviales","El Vertido de Plásticos,","Los Vertidos de Petróleo",
"La Actividad Minera en Alta Mar","El Cambio climático")




seguir = True


while seguir:
    opcion = int(input(f"Ingrese un numero entre 1 y {len(factores)}:  "))
    if opcion > len(factores):
        print("ERROR. No tenemos tantos factores!!")
    elif opcion == 0:
        print("JUEGO TERMINADO!")
        seguir = False
    else:
        print(factores[opcion - 1])









