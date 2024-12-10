# Escribir un programa en el que se pregunte al usuario
# por una frase y una letra, y muestre por pantalla el
# número de veces que aparece la letra en la frase.


""" Conteo de letras

Entradas:
frase (str): Frase ingresada por el usuario
letra (str): letra ingresada por el usuario

Salidas:
(str): print indicando cuantas veces se encuentra la letra en la frase """

frase = input("Introduzca una frase:\n")
letra = input("Introduzca una letra:\n")
i = 0

for n in frase:
    if n == letra:
        i += 1
print(f"La letra {letra} se encuentra {i} veces en la frase '{frase}'")