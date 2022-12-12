# TALLER PYTHON - N°3
# Autor: Julián Rodriguez
# Fecha: DIC-12-2022
# AA3-EV1 TALLER 3


from datetime import date

hoy = date.today()
i = 0
print("Bienvenido\nFecha actual: ", (hoy))
print("\n---------------------------------")


a = int(input('Ingrese el valor de A: '))
b = int(input('Ingrese el valor de B: '))
c = int(input('Ingrese el valor de C: '))

if (a == b) and (a == c):
    mayor = 'LOS 3 NUMEROS SON IGUALES'
else:
    if (a > b) and (a > c):
        mayor = 'A'
    elif (b > a) and (b > c):
        mayor = 'B'
    else:
        mayor = 'C'

print('El número mayor es %s: ' % (mayor) if len(mayor) == 1 else mayor)
print("\n---------------------------------\n")

materias = ['BackEnd', 'FrontEnd', 'Data scientist',
            'Data Analys', 'FullStack', 'Diseño Gráfico']

print(
    "A continuación podrá ver el listado de opciones disponibles para estudiar:\n")

# Se que no va en este módulo, pero me pareció interesante probar.
for materia in materias:
    print('Escriba: [%d] si desea estudiar: %s' % (i, materia))
    i += 1

matricular = int(input(
    "Ingrese el número de la carrera a la cual desea matricular: "))
print("\n---------------------------------")

if matricular >= len(materias):
    quit('Carrera no encontrada')
else:
    print('Bienvenido a la carrerea de:',  materias[matricular].upper())
print("\n---------------------------------")

if matricular == 5:
    print('USTED NO ES UN DESARROLLADOR DE SOFTWARE')
else:
    print('USTED ES UN DESARROLLADOR DE SOFTWARE')

print("\n--THIS IS THE END \n")
