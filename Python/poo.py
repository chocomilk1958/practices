# Programación Orientada a Objetos (POO).

# Creación de clases:
class Coche():    # Una clase es la contenedora de todos los metodos, objetos, etc de un programa.

# Creación de constructor:
    def __init__(self):    # Un constructor es un metodo que define los atributos de una clase.
        # Aquí los atributos van con "__" ya que esto significa que la encapsulación será de tipo privada. 
        # La encapsulación se refiere a si se puede modificar o acceder el atributo/estado de un objeto fuera de la clase.
        
        self.__largoChasis = 250

        self.__anchoChasis = 120

        self.__ruedas = 4
    
        self.__enMarcha = False

# Creación de metodos:
    def arrancar(self, arrancamos):    # Un metodo es una función pero que pertenece a una clase.
        self.__enMarcha = arrancamos

        if self.__enMarcha:
            analisis = self.__analisisCoche()

        if self.__enMarcha and analisis:
            return "El coche está en marcha"

        else:
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

    def __analisisCoche(self):    # Esto es un metodo de encapsulación privada, solo puede ser llamado dentro de la clase.
        print("Realizando chequeo interno...")

        self.__aceite = "OK"

        self.__gasolina = "OK"

        self.__puertasCerradas = "OK"

        if self.__aceite == "OK" and self.__gasolina == "OK" and self.__puertasCerradas == "OK":
            return True

        else:
            return False

# Instanciación de la clase/objeto de la clase:
miCoche = Coche()    # Un objeto es una instancia de la clase, contiene sus metodos.

# Operador punto (pseudocodigo):
print(miCoche.arrancar(True))    # El operador punto se utiliza para acceder a los atributos o metodos de un objeto.
                                 # El coche quiere arrancar (True).

miCoche.estado

print("")    # Espacio para separar los objetos en la consola.

# Segunda instanciación de clase:
miCoche2 = Coche()

print(miCoche2.arrancar(False))    # No quieres arrancar el coche (False).

miCoche2.estado()