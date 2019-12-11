# Modulo json para cargar datos "practica" II-2.

# Importamos el modulo json:
import json

# Creación de funciones:
def get_fav_color():
    """Obtener el color favorito del usuario."""

    fichero = 'C:\\Users\\usuario w10\\Documents\\Desarrollo\\Practicas - estudios\\Archivos\\Practicas\\colorfav.json'    # Ruta absoluta.

    try:
        with open(fichero) as f_obj:
            colorfav = json.load(f_obj)
    
    except:
        print("El fichero no existe o la ruta no es correcta. Por favor, revisa bien.",)

    else:
        print("Tu color favorito es:", colorfav, "obvio que lo ibamos a recordar!")

get_fav_color()