# Imagina que acabas de abrir una nueva cuenta de ahorros que te
# ofrece el 4% de interés al año. Estos ahorros debido a
# intereses, que no se cobran hasta finales de año, se te añaden
# al balance final de tu cuenta de ahorros. Escribir un programa
# que comience leyendo la cantidad de dinero depositada en la
# cuenta de ahorros, introducida por el usuario. Después el
# programa debe calcular y mostrar por pantalla la cantidad de
# ahorros tras el primer, segundo y tercer años. Redondear cada
# cantidad a dos decimales.

cantidad_deposito_ahorros = int(input("Ingrese la cantidad depositada en la cuenta de ahorros: "))
interes_anual = 0.04

anio = 1
while anio <= 3:
    cantidad_ahorro_actual = round((cantidad_deposito_ahorros*(interes_anual+1)), 2)
    print(cantidad_ahorro_actual)
    cantidad_deposito_ahorros = cantidad_ahorro_actual
    anio += 1
