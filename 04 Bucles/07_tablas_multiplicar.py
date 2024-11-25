# Escribir un programa que muestre por pantalla
# la tabla de multiplicar del 1 al 10.

""" Tabla del 1 al 10

Entradas:
x (int): tabla de multiplicar
n (Tipo): contador

Salidas:
(Tipo): Resultado esperado """

for x in range (1, 11):
    for n in range (1, 11):
        print(x*n, end="\t")
    print("")