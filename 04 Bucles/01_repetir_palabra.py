# Escribir un programa que pida al usuario una palabra
# y la muestre por pantalla 10 veces.

""" Dada una palabra ingresada por el usuario, repetirla 10 veces.

Variables:
palabra (str): palabra 
variable_2 (Tipo): [Descripción]

Resultado:
(str): palabra repetida 10 veces """

palabra = input("Ingrese una palabra: ")
contador = 0

while contador < 10:
    print(palabra)
    contador += 1

# word = input("Introduce una palabra: ")
# for i in range(10):
#     print(word)
