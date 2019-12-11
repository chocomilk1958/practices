# La modularización es dividir un programa en porciones, a los que se les llama "modulos". Este archivo será utilizado como modulo para el archivo de nombre "celular2.py"

# Código de ejemplo:
class Celular():
    def __init__(self, sistemaOperativo = "Android"):
        self.__sistemaOperativo = sistemaOperativo

        self.__almacenamiento = "Vacio"

        self.__root = False

        self.__formateo = False

    def analisis(self):
        print("-" * 22)

        print("REALIZANDO ANALISIS...")

        print("-" * 22)

        print("Sistema Operativo:", self.__sistemaOperativo, "\nAlmacenamiento:", self.__almacenamiento, "\nRoot:", self.__root)

    def formatear(self):
        while True:
            self.__select = input("Esta seguro que desea formatear?:").lower()

            if self.__select == "si":
                if self.__almacenamiento != "Vacio":
                    print("Formateando dispositivo...")

                    print("FORMATEO EXITOSO!")

                    self.__almacenamiento = "Vacio"

                    self.__formateo = True

                else:
                    print("Tu almacenamiento está vacio. Sin nada que borrar")

            elif self.__select == "no":
                print("Saliendo del formateo")
                
            else:
                print("Solo se admite como respuesta 'Si o No'")

    def rootear(self):
        if self.__formateo or self.__almacenamiento == "Vacio":
            if not self.__root:
                print("Dispositivo rooteado. PERMISOS DE SUPERUSUARIO CONCEDIDOS")

                self.__root = True

            else:
                print("El dispositivo ya está rooteado")

        else:
            print("Tu dispositivo necesita ser formateado o tener el almacenamiento vacio para realizar un rooteo")

    def descargarArchivos(self):
        print("Descargando 8 GB de archivo/s...")

        self.__almacenamiento = "Lleno"

        print("Almacenamiento lleno!!")