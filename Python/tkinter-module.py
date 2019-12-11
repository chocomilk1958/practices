# Principios del modulo TKinter, para interfaces gráficas.

# Importar modulo:
import tkinter as app

# Creación de la raíz:
root = app.Tk()               # Contenedor base de toda la interfaz.

# Ponerle titulo a la ventana:
root.title("Basic Interface")

# Ponerle un icono a la ventana:
root.iconbitmap('')                 # Este metodo nos pide una ruta que introduciremos como parametro.

# Activar o desactivar la redimensión de la ventana:
root.resizable(1,1)                                     # 0 es False y 1 True.

# Darle tamaño a la ventana:
root.geometry("640x480")

# Crear un botón y asignarlo a la ventana:
button = app.Button(root, text="Clickeame", command=None)   # Pasamos la raíz como primer parametro, a continuación el texto del botón y por ultimo la función del mismo.

button.pack()   # El metodo pack() agrega el botón a su contenedor.

# Bucle de aplicación, es como un bucle while True:
root.mainloop()