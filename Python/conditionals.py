# Mensaje de bienvenida:
print(
    "-----------------------------------\
    \nPrograma de evaluacion de alumnos.\
    \n-----------------------------------"
    )

# Entrada de datos con el teclado:
entrada = float(input("Introduzca la nota del alumno: "))

# Función para la evaluación de alumnos:
def evaluarAlumno(nota):
    evaluacion = "aprobado."

    if nota <6:
        evaluacion = "desaprobado."

    return evaluacion

print(evaluarAlumno(entrada))