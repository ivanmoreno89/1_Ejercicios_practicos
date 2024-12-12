# Escribir un programa que cree un diccionario simulando una cesta de compra.
# El programa debe preguntar el artículo y su precio y añadir el par al
# diccionario, hasta que el usuario decida terminar. Después se debe mostrar
# por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra	
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	…
# Total	Coste

""" Cesta de compras

Entradas:
cesta_compras (dict): Diccionario cesta de compras vacío.
choice (str): variable de decisión.
articulo (str): llave artículo en el diccionario.
valor (str): valor del artículo.
total_cesta (int): Suma total de valores de articulos.


Salidas:
(dict): Diccionario cesta de compras lleno """

cesta_compra = {}
choice = 'si'

while choice == 'si':
    articulo = input('Qué articulo desea agregar?:\n')
    valor = int(input(f'Ingrese el precio del articulo {articulo}:\n'))
    cesta_compra[articulo] = valor
    choice = input('Desea agregar información adicional (si/no):\n')

total_cesta = sum(cesta_compra.values())
print('La cesta de compra tiene los siguientes articulos:\n')
for articulo, valor in cesta_compra.items():
    print(articulo, ': ', valor)
print(f' El total de los articulos es de {total_cesta}')

# cesta = {}
# continuar = True
# while continuar:
#     item = input('Introduce un artículo: ')
#     precio = float(input('Introduce el precio de ' + item + ': '))
#     cesta[item] = precio
#     continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
# coste = 0
# print('Lista de la compra')
# for item, precio in cesta.items():
#     print(item, '\t', precio)
#     coste += precio
# print('Coste total: ', coste)
