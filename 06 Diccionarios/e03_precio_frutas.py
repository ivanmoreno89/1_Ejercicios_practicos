# Escribir un programa que guarde en un diccionario los precios
# de las frutas de la tabla, pregunte al usuario por una fruta,
# un número de kilos y muestre por pantalla el precio de ese
# número de kilos de fruta. Si la fruta no está en el diccionario
# debe mostrar un mensaje informando de ello.
#
# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

""" Precio de las frutas

Entradas:
fruits (dict): Diccionario con frutas y precios
user_fruit (str): Fruta ingresada por el usuario
cant_fruit (int): Cantidad a comprar
cost_fruit (float): multiplicación entre cant_fruit y el valor de user_fruit 

Salidas:
(str): Print con costo total de las frutas """

fruits = {
    'platano': 1.35,
    'manzana': 0.80,
    'pera': 0.85,
    'naranja': 0.70
}

print(fruits)
user_fruit = input('Ingrese la fruta que desea comprar:\n')

if user_fruit in fruits:
    print(fruits[user_fruit])
    cant_fruit = int(input('Ingrese la cantidad que desea comprar:\n'))
    cost_fruit = fruits[user_fruit]*cant_fruit
    print(f'El precio de {cant_fruit}un. de {user_fruit} es: {cost_fruit}')
else:
    print(f"La fruta {user_fruit} no se encuentra en el listado")

# frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
# fruta = input('¿Qué fruta quieres? ').title()
# kg = float(input('¿Cuántos kilos? '))
# if fruta in frutas:
#     print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
# else: 
#     print("Lo siento, la fruta", fruta, "no está disponible.")
