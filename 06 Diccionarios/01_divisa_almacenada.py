# Escribir un programa que guarde en una variable
# el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su
# símbolo o un mensaje de aviso si la divisa no está
# en el diccionario.

""" Divisas almacenadas

Entradas:
diccionario (Dict): Diccionario de divisas
user_divisa (str): divisa ingresada por el usuario
divisa (str): Key del diccionario

Salidas:
(str): Print informando que la divisa ingresada por el
usuario se encuentra o no en el diccionario """

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