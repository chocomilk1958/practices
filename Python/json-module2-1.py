# Modulo json para guardar datos "practica" II-1.

# Importamos el modulo json:
import json

# Creación de funciones:
def set_fav_color():
    """Guardar el color favorito del usuario."""

    fichero = 'colorfav.json'    # La ruta introducida es una ruta relativa, no absoluta.
                                 # El programa solo buscara el archivo 'colorfav.json' en el directorio actual hasta encontrarlo,
                                 # de lo contrario creara uno.

    colorfav = input("Dime tu color favorito: ")

    with open(fichero, 'w') as f_obj:
        json.dump(colorfav, f_obj)

        print("Recordaremos tu color favorito:", colorfav)

set_fav_color()