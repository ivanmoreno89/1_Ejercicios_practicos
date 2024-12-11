# La pizzería Bella Napoli ofrece pizzas vegetarianas y no
# vegetarianas a sus clientes. Los ingredientes para cada
# tipo de pizza aparecen a continuación:

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere
# una pizza vegetariana o no, y en función de su respuesta
# le muestre un menú con los ingredientes disponibles para
# que elija. Solo se puede eligir un ingrediente además de
# la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida
# es vegetariana o no y todos los ingredientes que lleva.

""" Dado un tipo de pizza, presentar los ingredientes y mostrar un mensaje con toda la información  

Variables:
tipo_pizza (str): Tipo de pizza
ingrediente (str): ingrediente seleccionado

Resultado:
(str): Mensaje que indique la pizza seleccionada y el ingrediente """


# Pregunta al cliente qué tipo de pizza quiere
tipo_pizza = input("Qué tipo de pizza quiere (Vegetariana o No Vegetariana)?: ")
ingrediente = 0

# Condicional para seleccionar ingredientes
if tipo_pizza.lower() == "vegetariana":
    print("Los ingredientes de la pizza vegetariana son: \n 1. Pimiento \n 2. Tofu \n Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas")
    ingrediente = input("Digite el ingrediente de la lista: ")
elif tipo_pizza.lower() == "no vegetariana":
    print("Los ingredientes de la pizza no vegetariana son: \n 1. Pepperoni \n 2. Jamón \n 3. Salmón \n Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas")
    ingrediente = input("Digite el ingrediente de la lista: ")
else:
    print("No seleccionó una de las 2 pizzas ofrecidas")

# Mensaje con información de la pizza y los ingredientes
print(f"La pizza seleccionada fue {tipo_pizza.lower()} y los ingredientes son: \n 1. Mozzarella \n 2. Tomate \n 3. {ingrediente}")
