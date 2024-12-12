# Escribir un programa que cree un diccionario de traducción
# español-inglés. El usuario introducirá las palabras en
# español e inglés separadas por dos puntos, y cada par
# <palabra>:<traducción> separados por comas. El programa debe
# crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario
# para traducir la palabra a palabras. Si una palabra no está
# en el diccionario debe dejarla sin traducir.

""" Traductor de Frase

Entradas:
traductor (dict): Diccionario vacio
texto (str): Texto ingresado por el usuario según requerimiento

Salidas:
(str): frase traducida """

traductor = {}

texto = input('Ingrese las palabras en español e ingles separadas por puntos y cada bloque separado por comas:\n')

for x in texto.split(','):
    spa, eng = x.split(':')
    traductor[spa] = eng
print(traductor)
frase = input('Escribe la frase a traducir:\n')
for i in frase.split():
    if i in traductor:
        print(traductor[i])
    else:
        print(i)
