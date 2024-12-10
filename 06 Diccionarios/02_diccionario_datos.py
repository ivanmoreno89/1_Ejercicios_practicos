# Escribir un programa que pregunte al usuario su nombre, edad,
# dirección y teléfono y lo guarde en un diccionario. Después
# debe mostrar por pantalla el mensaje <nombre> tiene <edad>años,
# vive en <dirección> y su número de teléfono es <teléfono>.

""" Diccionario datos personales

Entradas:
diccionario (dict): Diccionario con datos de nombre, edad, dirección y telefono vacios.

Salidas:
(dict): Diccionario con datos solicitados """

# Variables de entrada
diccionario = {
    'nombre': '',
    'edad': '',
    'ciudad': '',
    'telefono': '',
}
for key in diccionario:
    diccionario[key] = input(f'Ingrese su {key}:\n')

print(f'{diccionario["nombre"]} tiene {diccionario["edad"]} años, vive en {diccionario["ciudad"]} y su número de teléfono es {diccionario["telefono"]}')

# nombre = input('¿Cómo te llamas? ')
# edad = input('¿Cuántos años tienes? ')
# direccion = input('¿Cuál es tu dirección? ')
# telefono = input('¿Cuál es tu número de teléfono? ')
# persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
# print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])