# Escribir un programa que pregunte al usuario una cantidad a
# invertir, el interés anual y el número de años, y muestre por
# pantalla el capital obtenido en la inversión.

capital_inicial = int(input("Ingrese la cantidad que desea invertir: "))
tasa_interes = float(input("Ingrese el interés anual: "))
años = int(input("Ingrese el número de años para la inversión: "))

capital_inversion = round(capital_inicial*((1+(tasa_interes/100))**años), 2)

print(f"El capital obtenido en la inversión de {capital_inicial} en un periodo de {años} es de {capital_inversion}")

