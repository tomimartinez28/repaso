"""
Ejercicio 1: Triángulos

Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus parámetros y devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras, como resultado de la función. Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, use su función para calcular la longitud de la hipotenusa y muestre el resultado.
"""

# h ** 2= lado**2 + lado ** 2



def hipotenusa(lado1, lado2):
    hip = (lado1 ** 2 + lado2 **2 ) ** 0.5
    return hip

lado1 = float(input("ingrese la longitud del lado 1: "))
lado2 = float(input("ingrese la longitud del lado 2: "))

resul = round(hipotenusa(lado1, lado2), 2)

print(f"La hipotenusa mide: {resul}cms ")

