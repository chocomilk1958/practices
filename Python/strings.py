print('C:\algun\nombre')  # aquí \n significa nueva línea!

print(r'C:\algun\nombre')  # nota la r antes de la comilla

# Las cadenas de texto se pueden indexar (subíndices), 
# el primer carácter de la cadena tiene el índice 0. 
# No hay un tipo de dato para los caracteres; 
# un carácter es simplemente una cadena de longitud uno:

word = 'Python'

word[0]  # caracter en la posición 0,
         # osea "P"

print(word[0])

word[5]  # caracter en la posición 5, 
         # osea "n"

print(word[5])

# Los índices quizás sean números negativos, 
# para empezar a contar desde la derecha:

word[-1]  # último caracter

word[-2]  # ante último caracter

word[-6]  # primer caracter


# Además de los índices, las rebanadas también están soportadas. 

# Mientras que los índices son usados para obtener caracteres 
# individuales, las rebanadas te permiten obtener 
# sub-cadenas:

word = "Python"

print(word[0:4]) # esto imprime en pantalla la cadena "pyth"

# La función incorporada len() 
# devuelve la longitud de una cadena de texto:

word = 'supercalifrastilisticoespialidoso'

print(len(word)) # esto imprime en pantalla la longitud de "33" 
                 # caracteres