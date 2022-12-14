# Taller 4: Python
# Autor: Julian Rodriguez
# Fecha:10-Dic-2022

from datetime import date
exercises = ['Triangulos', 'Animales']
i = 0

today = date.today()
print('BIENVENIDO\n')
print('Hoy es el dia %s' % (today))

for item in exercises:
    print('Escriba: [%d] si desea estudiar: %s' % (i, item))
    i += 1

exercise = int(input('Por favor ingrese una opción valida: '))

if exercise < 0 or exercise > len(exercises)-1:
    quit('Opcion no valida')

elif exercise == 0:
    print('\n------------------')
    print('Ejercicios de las clases de los triangulos')
    a = int(input('Dígita el valor de A: '))
    b = int(input('Dígita el valor de B: '))
    c = int(input('Dígita el valor de C: '))

    if a == b and a == c and b == c:
        tipo = 'EQUILATERO'
    else:
        if a == b or b == c or a == c:
            tipo = 'ISOSELES'
        else:
            tipo = 'ESCALENO'
    print('El triangulo es %s\n' % tipo)
else:
    animales = ['Leon', 'Mariposa', 'Lobo', 'Tigre', 'Perro']
    zonas = ['Sabana', 'Bosque', 'Bosque', 'Selva', 'Ciudad']

    i = 0
    attempts = 0

    for animal in animales:
        print('Escriba: [%d] si desea estudiar: %s' % (i, animal))
        i += 1

    while attempts <= 10 or animalChoise in locals():

        animalChoise = int(input('Digite numero del animal: '))

        if animalChoise > len(animales) or animalChoise < 0:
            print('Opción no valida')
            attempts += 1
            continue

        animalPrint = animales[animalChoise]
        print('------------------')
        print('¡GRAN ELECCIÓN!\n',
              'La' if 'a' in animalPrint[-2:] else 'El', '%s es un animal Genial\n' % animalPrint.upper(), end='')
        print('ZONA RESIDENCIA: %s' % (zonas[animalChoise].upper()))

# print('---FIN---')
