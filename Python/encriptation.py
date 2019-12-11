# Programa para encriptar mensajes.


# Función para encriptar:
abc = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ").lower()

mensaje = input("Ingresa el mensaje que quieras encriptar: ")

k = (int(input("Ingresa cuantos dígitos quieres saltarte: ")))

mensajeCifrado = ""

for i in mensaje:
    if i in abc:
     mensajeCifrado += abc[ (abc.index(i) + k) % (len(abc)) ]
    else:
        mensajeCifrado += i

print(mensajeCifrado)