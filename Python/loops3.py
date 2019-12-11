# Practica loops:
# Crea un programa que pida números infinitamente,
# los números deben ser cada vez mayores, de lo contrario el programa finalizara.

# Entrada de números:
num = int(input("Introduce un numero: "))

numDos = int(input("Introduce un numero mayor que " + str(num) + ": "))

# Bucle:
while numDos > num:

    num = numDos

    numDos = int(input("Introduce un numero mayor que " + str(num) + ": "))

print("BEEP - BOOP. ERROR!")
print(str(numDos) + " no es mayor que: " + str(num))