# Programación Orientada a Objetos (POO) III. "Herencia: Metodo Super".

# Clases:
class Persona():    # Clase padre(superClass).
    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre = nombre
        
        self.edad = edad

        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        print("Nombre:", self.nombre, " Edad:", self.edad, " Residencia:" , self.lugarResidencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):

        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)    # El metodo "super" permite acceder a los metodos de otra clase. En este ejemplo el nombre del empleado, su edad y su residencia van a ser transportados al constructor de la clase "Persona", mientras que los otros argumentos serán usados en la clase "Empleado"

        self.salario = salario
        
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion()    # En este caso el metodo "super" llamara al metodo "descripcion" de la clase "Persona",
                                 # y luego imprimirá la linea de abajo.

        print("Salario:", self.salario, " Antiguedad:", self.antiguedad)

antonio = Empleado(20000, 25, "Antonio", 55, "España")   # Instancia de clase "Empleado".

antonio.descripcion()    # Llamamos al metodo "descripcion" de la clase "Empleado".

print(isinstance(antonio, Empleado))    # El metodo "isinstance" sirve para saber si X objeto es instancia de X clase.
pepe = Persona("Pepe", 25, "Argentina")

print(isinstance(pepe, Persona))