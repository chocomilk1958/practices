def userPass(age):
    if age >= 18:
        return print("Acceso garantizado.")
    else:
        return print("Acceso NO garantizado, debes ser mayor de edad.")

while True:
    print("Verificacion de acceso...")

    age_user = int(input("Por favor, introduzca su edad: "))

    print("Verificando...")
    
    userPass(age_user)