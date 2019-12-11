# Generadores.

# Creación del generador:
def NumerosPares(limite):   
    num = 1
    while num < limite:
        yield num * 2
        num += 1

# Creación del objeto iterable:
devuelvePares = NumerosPares(10)

# Mostrar en consola uno a uno los dígitos:
print(next(devuelvePares))