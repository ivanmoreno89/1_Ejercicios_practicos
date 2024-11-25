# Escribir un programa que guarde en una variable
# el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su
# símbolo o un mensaje de aviso si la divisa no está
# en el diccionario.

""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

# Variables de entrada
diccionario = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}
user_divisa = input("Escriba la divisa:\n")
for divisa in diccionario:
    if divisa == user_divisa:
        print(diccionario[divisa])
    else:
        print(f"La divisa {user_divisa} no se encuentra almacenada en el diccionario")
        break

# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda = input("Introduce una divisa: ")
# print(monedas.get(moneda.title(), "La divisa no está."))

# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda = input("Introduce una divisa: ")
# if moneda.title() in monedas:
#     print(monedas[moneda.title()])
# else:
#     print("La divisa no está.")