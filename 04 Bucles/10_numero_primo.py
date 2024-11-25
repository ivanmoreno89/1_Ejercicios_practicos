# Escribir un programa que pida al usuario un
# número entero y muestre por pantalla si es
# un número primo o no.


""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

numero = int(input("Escriba un número entero:\n"))
i = 2
while numero % i != 0:
    i += 1

if i == numero:
    print("es primo")
else:
    print("no es primo")
