# Una panadería vende barras de pan a 3.49€ cada una. El pan que
# no es el día tiene un descuento del 60%. Escribir un programa
# que comience leyendo el número de barras vendidas que no son
# del día. Después el programa debe mostrar el precio habitual
# de una barra de pan, el descuento que se le hace por no ser
# fresca y el coste final total.

precio_pan_freco=3.49
descuento_pan_viejo=0.6

cantidad_pan_barra = int(input("¿Cuántas barras de pan viejo se vendieron?: "))
print(f"Una barra de pan fresco cuesta {precio_pan_freco} euros")
print("El precio del pan viejo tiene un descuento del 60%")
precio_total = round((cantidad_pan_barra * precio_pan_freco * (1 - descuento_pan_viejo)), 2)
print(f"El precio final del pedido de {cantidad_pan_barra} panes barra es de {precio_total} euros")