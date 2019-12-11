# Programación Orientada a Objetos (POO) IV. "Polimorfismo".

# Clases:
class Coche():
    def desplazamiento(self):
        print("Yo soy un coche y me desplazo con 4 ruedas.")
    
class Moto():
    def desplazamiento(self):
        print("Yo soy una moto y me desplazo con 2 ruedas.")

class Camion():
    def desplazamiento(self):
        print("Yo soy un camion y me desplazo con 6 ruedas.")

def vehiculoDesplazamiento(veh):    # Esta función lo que hace es pedir por parametro un objeto.
                                    # (En este caso un objeto de tipo "Moto"), 
                                    # y luego llama al metodo "desplazamiento" correspondiente al tipo de objeto 
                                    # ( Vehiculo "Moto".desplazamiento() ).
    veh.desplazamiento()

vehiculo = Moto()    # Creamos la instancia de la clase "Moto".

vehiculoDesplazamiento(vehiculo)    # Llamamos a la función y le pasamos por parametro el objeto "Vehiculo" que es una instancia de "Moto".

# En resumen, el polimorfismo es lo que se utiliza para denominar un metodo que sirva para varios objetos y que a su vez este metodo modifique su forma.