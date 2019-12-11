print("Asignaturas optativas. Año 2019")
print("Asignaturas optativas: Informática gráfica - Pruebas de software -\
 Usabilidad y accesibilidad")
opcion = input("Elige una asignatura: ")

asignatura = opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software",
"usabilidad y accesibilidad"):
    print("Asignatura elegida es: " + asignatura)

else:
    print("La asignatura escogida no está contemplada")