# Escribir un programa que almacene el abecedario en
# una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de 3, y muestre por pantalla la
# lista resultante.

""" Eliminar posición de una lista

Entradas:
n (int): Valor inicial
abc (list): Abecedario en lista

Salidas:
(str): print con abecedario filtrando posiciones multiplos de 3 """

#Variables
n = 0
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Bucle
print(abc)
for n in range(len(abc), 1, -1):
    if n % 3 == 0:
        abc.pop(n-1)
            
# Mensaje con abecedario filtrado
print(abc)