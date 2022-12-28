# Trabajo con colecciones de valores

import random

ans = ['NO', 'SI']
types = ['Bicho', 'Dragón', 'Eléctrico', 'Hada', 'Lucha', 'Fuego', 'Volador', 'Fantasma',
         'Planta', 'Tierra', 'Hielo', 'Normal', 'Veneno', 'Psíquico', 'Roca', 'Acero', 'Agua']
randomValue = random.randint(0, len(types))
# print(randomValue)
print('Felicidades, ha obtenido el tipo: %s' % (types[randomValue]))
# range()

print('Para eliminar un tipo de pokemon escriba:')
i = 0
for tipo in types:
    print('{0} - {1}'.format(i, tipo))
    i += 1
print()

exit = ''
delChoice = ''
confirmation = ''

while True:

    if exit.upper() == 'S' or (delChoice != '' and confirmation == 1):
        break

    delChoice = input(
        'Ingrese el valor del listado de 0 a {0}: '.format(len(types)-1))

    try:
        delChoice = int(delChoice)

        if delChoice >= 0 and delChoice <= len(types)-1:
            print('¿Esta seguro de eliminar el tipo:{0}'.format(
                types[delChoice]), end='\n')
            y = 0

            for choiseans in ans:
                print('{0}-{1}'.format(y, choiseans), end='\t')
                y += 1

            while True:

                confirmation = input('\nDígite su respuesta: ')
                try:
                    confirmation = int(confirmation)
                    if (confirmation >= 0 and confirmation <= 1):
                        break
                    else:
                        print('opción invalida')

                except ValueError:
                    exit = input(
                        'Opcion invalida.\nPara abandonar el proceso oprima la tecla S: ')
                    if exit.upper() == 'S':
                        break

    except ValueError:
        print('No ha seleccionado una opción valida:\n')

        exit = input(
            'Opcion invalida\nPara abandonar el proceso oprima la tecla S: ')
        if exit.upper() == 'S':
            break

if exit == 'S':
    print('El proceso finalizó de forma interrumpida por el usuario,\nGracias.')
else:
    print('Confirmación\nHa eliminado el tipo: {0}\nDel listado de tipos:'.format(
        types.pop(delChoice)), end='\n')
    print('\nLista de tipos actualizada: ', end='\n[ ')

    i = 0
    for tipo in types:
        print('{0}-{1}'.format(i, tipo), end=' ░ ' if i < len(types)-1 else '')
        i += 1
    print(' ]')
