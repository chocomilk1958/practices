# Crea un programa que pida números positivos indefinidamente. El programa termina
# cuando se introduce un número negativo. Finalmente el programa muestras la suma de
# todos los números introducidos.

# Entrada de números:
num = int(input("Introduce un numero positivo: "))

suma = 0

# Bucle de entrada y suma de números:
while num > 0:

    suma+=num

    num = int(input("Introduce un numero positivo: "))

# Si el bucle no se cumple/deja de cumplirse:
print("BEEP BOOP - ERROR")
print(str(num), "no es un numero positivo.")
print("La suma de todos los numeros que has introducido es:", str(suma))