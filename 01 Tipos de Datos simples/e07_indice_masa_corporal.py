# Escribir un programa que pida al usuario su peso (en kg) y
# estatura (en metros), calcule el índice de masa corporal y lo
# almacene en una variable, y muestre por pantalla la frase "Tu
# índice de masa corporal es <imc>" donde <imc> es el índice
# de masa corporal calculado redondeado con dos decimales.

peso = int(input("Ingrese el peso: "))
altura = float(input("Ingrese la altura: "))
imc = ((peso)/(altura * altura))
print("Tu índice de masa corporal es: ", imc)