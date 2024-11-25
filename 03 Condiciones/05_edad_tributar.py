# Para tributar un determinado impuesto se debe ser mayor
# de 16 años y tener unos ingresos iguales o superiores a
# 1000 € mensuales. Escribir un programa que pregunte al
# usuario su edad y sus ingresos mensuales y muestre por
# pantalla si el usuario tiene que tributar o no.

edad = int(input("Ingrese su edad: "))

if edad >= 16:
    ingresos = int(input("Cuáles son sus ingresos mensuales?: "))
    if ingresos > 1000:
        print("De acuerdo con los datos ingresados, ud está obligado a tributar este año")
    else:
        print("Teniendo en cuenta que sus ingresos son menores a 1000 €, usted no no está obligado a tributar este año")
else:
    print("Teniendo en cuenta que usted es menor de edad, no está obligado a tributar")

# ingresos = int(input("Cuáles son sus ingresos mensuales?: "))
# if edad >= 16 and ingresos > 1000:
#     print("De acuerdo con los datos ingresados, ud está obligado a tributar este año")
# else:
#     print("De acuerdo con los datos ingresados, ud no está obligado a tributar este año")
