# Escribir un programa que permita gestionar la base
# de datos de clientes de una empresa. Los clientes
# se guardarán en un diccionario en el que la clave
# de cada cliente será su NIF, y el valor será otro
# diccionario con los datos del cliente (nombre,
# dirección, teléfono, correo, preferente), donde
# preferente tendrá el valor True si se trata de un
# cliente preferente. El programa debe preguntar al
# usuario por una opción del siguiente menú: (1) Añadir
# cliente, (2) Eliminar cliente, (3) Mostrar cliente,
# (4) Listar todos los clientes, (5) Listar clientes
# preferentes, (6) Terminar.
# 
# En función de la opción elegida el programa tendrá
# que hacer lo siguiente:
# Preguntar los datos del cliente, crear un diccionario
# con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos
# de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos
# con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de
# datos con su NIF y nombre.
# Terminar el programa.

""" BD Menu clientes

Entradas:
clientes (dict): Diccionario de clientes.
nif_cliente (dict): Datos de clientes.
opt (int): valor del menú.
nif (int): NIF del cliente.
nif_delete (int): NIF del cliente a eliminar.
nif_mostrar (int): NIF del cliente a mostrar.


Salidas:
(str): Información solicitada por menú """

clientes = {}
nif_cliente = {}
opt = 0
while opt != 6:
    if opt == 1:
        nif = input('Ingrese el NIF del cliente:\n')
        nif_cliente = {'nombre': '',
                        'dirección': '',
                        'teléfono': '',
                        'correo': '',
                        'preferente': ''
                        }
        for key in nif_cliente:
            nif_cliente[key] = input(f'Ingrese la información de {key} del cliente:\n')
        print(nif_cliente)
        clientes[nif] = nif_cliente

    if opt == 2:
        print(clientes)
        nif_delete = input('Qué cliente desea eliminar?:\n')
        print(f'El cliente {nif_delete} será eliminado')
        clientes.pop(nif_delete)

    if opt == 3:
        print(clientes.keys())
        nif_mostrar = input('Qué cliente desea mostrar?:\n')
        print(clientes.get(nif_mostrar))

    if opt == 4:
        for nif, nif_cliente in clientes.items():
            print(nif, '\t', nif_cliente)

    if opt == 5:
        for llave, valor in clientes.items():
            if valor['preferente'] == 'True':
                print(llave, valor['nombre'])

    opt = int(input('(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\n¿Qué acción desea realizar?:\n'))

# clientes = {}
# opcion = ''
# while opcion != '6':
#     if opcion == '1':
#         nif = input('Introduce NIF del cliente: ')
#         nombre = input('Introduce el nombre del cliente: ')
#         direccion = input('Introduce la dirección del cliente: ')
#         telefono = input('Introduce el teléfono del cliente: ')
#         email = input('Introduce el correo electrónico del cliente: ')
#         vip = input('¿Es un cliente preferente (S/N)? ')
#         cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
#         clientes[nif] = cliente
#     if opcion == '2':
#         nif = input('Introduce NIF del cliente: ')
#         if nif in clientes:
#             del clientes[nif]
#         else:
#             print('No existe el cliente con el nif', nif)
#     if opcion == '3':
#         nif = input('Introduce NIF del cliente: ')
#         if nif in clientes:
#             print('NIF:', nif)
#             for clave, valor in clientes[nif].items():
#                 print(clave.title() + ':', valor)
#         else:
#             print('No existe el cliente con el nif', nif)
#     if opcion == '4':
#         print('Lista de clientes')
#         for clave, valor in clientes.items():
#             print(clave, valor['nombre'])
#     if opcion == '5':
#         print('Lista de clientes preferentes')
#         for clave, valor in clientes.items():
#             if valor['preferente']:
#                 print(clave, valor['nombre'])
#     opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
