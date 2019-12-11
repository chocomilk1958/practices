# Excepciones.

# Solicitar números al usuario:
while True:    # Bucle indeterminado que solo finaliza al insertar datos validos.
    try:
        num1 = float(input("Introduce un número: "))

        num2 = float(input("Introduce otro número: "))

        break    # Este "break" se encarga de finalizar con el bucle solo si se insertan
                 # datos validos en los "input" de arriba.
                 # De lo contrario se ejecuta el bucle indefinidamente.

    except ValueError:
        print("Introduce un número valido. Reintentalo!")

# Definicion de funciones:
def suma(n1, n2):    # Suma.
    return num1 + num2

def resta(n1, n2):    # Resta.
    return num1 - num2

# Imprimir resultados:
print(suma(num1, num2))    # Resultado de la suma.

print(resta(num1, num2))    # Resultado de la resta.