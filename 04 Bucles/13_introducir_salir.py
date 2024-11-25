# Escribir un programa que muestre el eco de todo
# lo que el usuario introduzca hasta que el usuario
# escriba "salir" que terminará.

""" [Resumen]

Entradas:
Variable_01 (Tipo): [Descripción]
Variable_02 (Tipo): [Descripción]

Salidas:
(Tipo): Resultado esperado """

frase = ""
while frase.lower() != "salir":
    frase = input("Escriba una frase:\n")
print("Ha salido exitosamente")

# while True:
#     frase = input("Introduce algo: ")
#     if frase == "salir":
#         break
#     print(frase)
