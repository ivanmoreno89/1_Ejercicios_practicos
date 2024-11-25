# Escribir un programa en el que se pregunte al usuario
# por una frase y una letra, y muestre por pantalla el
# número de veces que aparece la letra en la frase.


""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

frase = input("Introduzca una frase:\n")
letra = input("Introduzca una letra:\n")
i = 0

for n in frase:
    if n == letra:
        i += 1
print(f"La letra {letra} se encuentra {i} veces en la frase '{frase}'")