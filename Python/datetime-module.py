# Ejemplo del modulo datetime.

# Importamos el modulo "datetime" y "timedelta":
from datetime import datetime, timedelta

# Definimos fecha y hora actuales:
fechaHoy = datetime.now()

# Mostramos resultado:
print("Fecha y hora de hoy:", str(fechaHoy))

# Calculamos fecha futura (100 dias):
fechaFutura = fechaHoy + timedelta(days = 100)

# Mostramos fecha futura:
print("Dentro de 100 dias sera:", str(fechaFutura))

# Obtención de datos aislados:
print("El dia de hoy es:", str(fechaHoy.day)) # -Días

print("El mes de hoy es:", str(fechaHoy.month)) # -Mes

print("El año actual es:", str(fechaHoy.year)) # -Año

print("La hora actual es:", str(fechaHoy.hour)) # -Hora

print("Los minutos actuales son:", str(fechaHoy.minute)) # -Minutos

print("Los segundos actuales son:", str(fechaHoy.second)) # -Segundos

print("Los mmicrosegundos actuales son:", str(fechaHoy.microsecond)) # -Microsegundos
