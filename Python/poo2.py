# Programación Orientada a Objetos (POO) II. "Herencia y Herencia Multiple".

# Clase padre (Superclase):
class Vehiculo():

    def __init__(self, marca, modelo):    # Constructor.
        self.marca = marca

        self.modelo = modelo

        self.enMarcha = False

        self.acelerar = False

        self.frenar = False

    def arrancar(self):    # Funciones de la clase (metodos).
        self.enMarcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frenar = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enMarcha, "\nAcelerando:", self.acelerar, "\nFrenando:", self.frenar)

# Clase hija (Subclase):
class Moto(Vehiculo):    # Sintaxis de herencia: class MyClass(SuperClass).
    caballito = "No estoy haciendo el caballito"

    def hacerCaballito(self):
        if self.acelerar:
            self.caballito = "Estoy haciendo el caballito"

        else:
            self.caballito = "No puedo hacer el caballito, la moto no esta acelerando"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn Marcha:", self.enMarcha, "\nAcelerando:", self.acelerar, "\nFrenando:", self.frenar, "\nCaballito:", self.caballito)

class Furgoneta(Vehiculo):
    def carga(self, cargar = False):
        self.cargado = cargar

        if self.cargado:
            return "La furgoneta está cargada"

        else:
            return "La furgoneta no está cargada"

class VElectricos(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True
        

class BicicletaElectrica(VElectricos):    # Herencia multiple, siempre se da preferencia a la primera clase.
    pass

miMoto = Moto("Honda", "CBR")    # Llamamos al constructor de la Clase Padre mediante la creación del objeto "miMoto".

miMoto.hacerCaballito()

miMoto.estado()

print("")    # Separación.

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.estado()

print(miFurgoneta.carga(True))

print("")

miBici = BicicletaElectrica("Marca de bici", "Modelo de ejemplo")

miBici.estado()