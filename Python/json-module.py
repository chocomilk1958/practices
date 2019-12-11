# Modulo json para guardar y cargar datos.

# Importamos el modulo json:
import json

# Creación de funciones:
def saludar_usuario():
    """Saludar al usuario mediante el nombre."""

    # Ruta del fichero json para guardar/cargar datos:
    fichero = 'C:\\Users\\usuario w10\\Documents\\Desarrollo\\Practicas - estudios\\Archivos\\Practicas\\data.json'

    # El bloque try comprobará si hay datos dentro del fichero json, 
    # si no los hay pasara al "except":
    try:
        with open(fichero) as f_obj:
            user = json.load(f_obj)    # "json.load(f_obj)" se usa para cargar los datos 
                                       # del fichero a una variable.

    # Si este bloque se ejecuta nos pedira que ingresemos los datos solicitados:
    except:
        user = input("Introduce tu nombre de usuario: ")

        with open(fichero, 'w') as f_obj:
            json.dump(user, f_obj)    # "json.dump(datoParaGuardar, f_obj)" 
                                      # nos escribirá los datos introducidos al fichero.

            print("Te recordaremos,", user, "!!")
    
    # Si el bloque "try" se ejecuta correctamente y no pasa al "except", 
    # se ejecutara este bloque "else", el cual nos da la bienvenida:
    else:
        print("Bienvenido devuelta,", user, "!!")

# Llamada a la función:
saludar_usuario()

