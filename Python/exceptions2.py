# Excepciones II: Como lanzar excepciones manualmente con "raise".

# Solicitud de edad al usuario:
edad = int(input("Hola, me gustaria saber cuantos años tienes!!: "))

if edad < 0:    # Si la edad es negativa lanzará una excepción.
    raise TypeError("Esa edad no existe.")    # Podemos lanzar la excepción que queramos.

if edad < 10:
    print("Eres muy pequeño! :)")

elif edad < 20:
    print("Ya eres mayor.")

elif edad < 50:
    print("Buen día, señor.")

elif edad < 80:
    print("... Cuidado..")