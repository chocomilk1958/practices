# Metodos de cadena.

# Entrada de datos:

while True:
    nombre = input("Introduce tu nombre: ").capitalize()    # Y le aplicamos el metodo "capitalize" que lo que hace es convertir la primera letra de la cadena en Mayuscula,
                                                            # y las demás en Minusculas.

    if nombre.isalpha():    # El metodo "isalpha" nos devuelve "True" si la cadena está compuesta solo por letras. Los espacios NO CUENTAN.
        break

    else:
        print("Introduce un nombre correcto.")

print("Tu nombre es:", nombre)