# Escribir un programa que pregunte por una muestra de
# números, separados por comas, los guarde en una lista
# y muestre por pantalla su media y desviación típica.

""" Media y Desviación

Entradas:
cadena (str): cadena de valores ingresados por el usuario
lista (list): Lista con valores convertidos a int desde 'cadena'

Salidas:
(str): Print con resultados de media y desviación de los valores """

# Variables de entrada
cadena = input("Ingrese los valores separados por comas:\n")
cadena = list(cadena.replace(", ",""))
print(cadena)
lista = list(map(int, cadena))
suma = 0
suma_desv = 0
desv = 0

# Media
for num in lista:
    suma += num
media = suma / len(lista)
print(f"la media de la lista {lista} es: {media}")

# Desviación estandar
for num in lista:
    suma_desv += (num - media)**2
desv = ((suma_desv/len(lista))**(1/2))
print(f"La desviación tipica de la lista {lista} es: {desv}")

# Otra forma de resolverlo

# sample = input("Introduce una muestra de números separados por comas: ")
# sample = sample.split(',')
# n = len(sample)
# for i in range(n):
#     sample[i] = int(sample[i])
# sample = tuple(sample)
# sum = 0
# sumsq = 0
# for i in sample:
#     sum += i
#     sumsq += i**2
# mean = sum/n
# stdev = (sumsq/n-mean**2)**(1/2)
# print('La media es', mean, ', y la desviación típica es', stdev)