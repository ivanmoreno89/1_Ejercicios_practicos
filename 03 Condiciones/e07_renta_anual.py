# Los tramos impositivos para la declaración de la renta
# en un determinado país son los siguientes:
#
# Renta                   Tipo impositivo
# Menos de 10000€               5%
# Entre 10000€ y 20000€	        15%
# Entre 20000€ y 35000€	        20%
# Entre 35000€ y 60000€         30%
# Más de 60000€	                45%
# 
# Escribir un programa que pregunte al usuario su renta anual
# y muestre por pantalla el tipo impositivo que le corresponde.

""" Renta anual

Variables:
renta anual (int): valor de renta anual.
tipo_impositivo (float): cifra o porcentaje que se aplica para obtener como resultado la cuota íntegra.

Resultado:
(str): print con error de información ingresada o el valor a cancelar """

renta_anual = int(input("Ingrese su renta anual: "))
tipo_impositivo = float(0)

if renta_anual < 10000:
    tipo_impositivo = float(0.05)
elif renta_anual < 20000:
    tipo_impositivo = float(0.15)
elif renta_anual < 35000:
    tipo_impositivo = float(0.2)
elif renta_anual < 60000:
    tipo_impositivo = float(0.3)
elif renta_anual > 60000:
    tipo_impositivo = float(0.45)
else:
    print("Error en la información ingresada")

print(f"El tipo impositivo corresponde al {tipo_impositivo} y el valor a cancelar es de {tipo_impositivo*renta_anual}")
