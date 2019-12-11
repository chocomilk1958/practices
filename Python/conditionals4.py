# Programa de becas escolares.

# Datos para la beca:
distancia = float(input("¿A cuantos KM's vives de la escuela?: "))

num_hermanos = int(input("¿Cuantos hermanos tienes?: "))

salario_fam = float(input("Introduce el salario total de tu familia: "))

# Función para la beca:
def beca(dist, hermanos, salario):

# Si todo está bien:
    if dist > 40 and hermanos > 2 and salario <= 20000 or salario <= 20000:
        return print("Felicidades, usted ha ganado una beca!!")

# De lo contrario:
    else:
        return print("Lo siento, usted no cumple los requisitos para una beca.")

beca(distancia, num_hermanos, salario_fam)