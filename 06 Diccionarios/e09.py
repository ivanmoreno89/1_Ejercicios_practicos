# Escribir un programa que gestione las facturas pendientes de cobro
# de una empresa. Las facturas se almacenarán en un diccionario donde
# la clave de cada factura será el número de factura y el valor el
# coste de la factura. El programa debe preguntar al usuario si quiere
# añadir una nueva factura, pagar una existente o terminar. Si desea
# añadir una nueva factura se preguntará por el número de factura y
# su coste y se añadirá al diccionario. Si se desea pagar una factura
# se preguntará por el número de factura y se eliminará del diccionario.
# Después de cada operación el programa debe mostrar por pantalla la
# cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

""" [Descripción]

Entradas:
variable1 (type): [Descripción]
variable2 (type): [Descripción]
variable3 (type): [Descripción]

Salidas:
(type): [Descripción] """

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