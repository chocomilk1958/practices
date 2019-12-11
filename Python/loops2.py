# Mensaje de bienvenida:
print("-------------------\n\
Programa de conteo.\n\
-------------------")

# Número desde el cual se desea contar:
num = int(input("Desde que numero deseas contar?: "))

# Numero hasta el cual se desea contar:
numDos = int(input("Hasta cuanto quieres contar?: "))

# Conteo:
print("Ha elegido contar desde: ",num ,", hasta: ", numDos)

while num > numDos or num < numDos or num == numDos:
    if num > numDos:
            print(num, " / ", numDos)

            num-=1

            if num == numDos:
                break

    elif num < numDos:
        print(num, " / ", numDos)    

        num+=1
        
        if num == numDos:
            break

    elif num == numDos:
        print("Los numeros son iguales!")