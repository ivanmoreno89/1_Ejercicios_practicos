# Escribir un programa que cree un diccionario vacío y lo vaya llenado
# con información sobre una persona (por ejemplo nombre, edad, sexo,
# teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez
# que se añada un nuevo dato debe imprimirse el contenido del diccionario.

""" Datos personales

Entradas:
datos_personales (dict): Diccionario de datos vacío
choice (str): variable de decisión
llave (str): llave del diccionario
valor (str): valor del diccionario


Salidas:
(dict): Diccionario actualizado con datos personales """

datos_personales = {}
choice = 'si'

while choice == 'si':
    llave = input('Qué dato personal desea agregar?:\n')
    valor = input(f'Ingrese la información asociada al dato {llave}:\n')
    datos_personales[llave] = valor
    print(datos_personales)
    choice = input('Desea agregar información adicional (si/no):\n')

# persona = {}
# continuar = True
# while continuar:
#     clave = input('¿Qué dato quieres introducir? ')
#     valor = input(clave + ': ')
#     persona[clave] = valor
#     print(persona)
#     continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
