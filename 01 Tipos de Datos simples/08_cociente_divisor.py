# Escribir un programa que pida al usuario dos números enteros y
# muestre por pantalla la <n> entre <m> da un cociente <c> y un
# resto <r> donde <n> y <m> son los números introducidos por el
# usuario, y <c> y <r> son el cociente y el resto de la división
# entera respectivamente.

m = input("Escriba un primer número entero: ")
n = input("Escriba un segundo número entero: ")

cociente = int(m) // int(n)
residuo = int(m) % int(n)

print(f"El cociente de dividir {m} entre {n} es {cociente}")
print(f"El residuo de dividir {m} entre {n} es {residuo}")