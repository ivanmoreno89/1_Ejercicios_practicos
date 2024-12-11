# Escribir un programa que pregunte al usuario una
# cantidad a invertir, el interés anual y el número
# de años, y muestre por pantalla el capital obtenido
# en la inversión cada año que dura la inversión.

""" Capital obtenido en inversión anual

Entradas:
valor_invertir (int):   Valor de inversión ingresado por el usuario
interes_anual (float):  Valor de interes anual ingresado por el usuario
anios (int):            Duración de la inversión en años 
capital_inicial (int):  Capital al iniciar el año
capital_nuevo (int):    Capital a fin del año
n (int):                Contador

Salidas:
(str): Mensaje con el capital obtenido anualmente """

valor_invertir=int(input("Ingrese la cantidad que desea invertir:\n"))
interes_anual=float(input("Ingrese el interes anual sin el simbolo porcentaje:\n"))
anios=int(input("Ingrese los años que durará la inversión:\n"))

capital_inicial = valor_invertir

for n in range(anios):
    capital_final = round(capital_inicial*(1+interes_anual), 2)
    print(f"El capital acumulado para el año {anios} es de {capital_final}")
    capital_inicial = capital_final
