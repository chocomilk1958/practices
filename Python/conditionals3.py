# El presidente de la empresa siempre deberá tener el mejor salario, 
# de lo contrario, ERROR.

# Salarios:
salario_presidente = float(input("Introduce el salario del presidente de la empresa: "))
print("El salario es:", salario_presidente)

salario_director = float(input("Introduce el salario del director de la empresa: "))
print("El salario es:", salario_director)

salario_jefe_area = float(input("Introduce el salario del jefe de area de la empresa: "))
print("El salario es:", salario_jefe_area)

salario_administrativo = float(input("Introduce el salario del administrativo de la empresa: "))
print("El salario es:", salario_administrativo)

# Condicionales:
if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print("Todo correcto.")
else:
    print("Error.")