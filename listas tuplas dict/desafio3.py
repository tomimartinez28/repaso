"""
Desafío 3		
Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. No se podrán insertar nombres repetidos.

"""

agenda = {}
seguir = True


while seguir:
    nombre = input("Ingrese un nombre: ")
    while nombre in agenda:
        print("ERROR EL NOMBRE YA EXISTE. INGRESE OTRO")
        nombre = input("Ingrese un nombre: ") 
        
    email = input("Ingrese el mail: ")
    agenda[nombre] = email
    rta = input("Desea registrar otra persona? \nsi/no: ")
    if rta.lower() == "no":
        seguir = False


    

print("SU AGENDA ES: ")
print(agenda)


