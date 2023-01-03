# Trabajo con colecciones de valores

import random

CRUD = ['Salir', 'Crear', 'Leer', 'Actualizar', 'Elementar']
ans = ['NO', 'SI']
types = ['Bicho', 'Dragón', 'Eléctrico', 'Hada', 'Lucha', 'Fuego', 'Volador', 'Fantasma',
         'Planta', 'Tierra', 'Hielo', 'Normal', 'Veneno', 'Psíquico', 'Roca', 'Acero', 'Agua']
randomValue = random.randint(0, len(types)-1)
# print(randomValue)
print('Felicidades, ha obtenido el tipo: %s' % (types[randomValue]))
# range()

i = 0
for tipo in types:
    print('{0} - {1}'.format(i, tipo))
    i += 1
print()

i = 0
for option in CRUD:
    print('{0} - {1}'.format(i, option))
    i += 1

# Elección del tipo de acción que será ejecutada
while True:
    choiceCrud = input('Ingrese la opción que desea realizar: ')

    try:
        choiceCrud = int(choiceCrud)
        if choiceCrud >= 0 and choiceCrud <= len(CRUD):
            if (choiceCrud > 0):
                break
            else:
                exit()

    except ValueError:
        print('Opción invalida')

print('\nPara {0} un tipo de pokemon escriba: '.format(CRUD[choiceCrud]))

exit = ''
result = ''
confirmation = ''

# Procedimiento
while True:

    if exit.upper() == 'S' or (result != '' and confirmation == 1):
        break

    if CRUD[choiceCrud] == CRUD[1]:
        msg = 'Ingrese el nombre del tipo que desea crear: '

    else:
        msg = 'Ingrese el valor del listado de 0 a {0}: '.format(len(types)-1)

    try:
        result = input(msg)

        result = int(result) if (
            len(result) <= 2 and result != 'S') else result

        if type(result) != int and result.upper() == 'S':
            exit = result
            break

        print('¿Esta seguro de {0} el tipo: {1}'.format(CRUD[choiceCrud],
                                                        types[result] if type(result) == int else result), end='\n')
        break

        if result >= 0 and result <= len(types)-1:

            print('¿Esta seguro de eliminar el tipo: {0}'.format(
                types[result] if result >= 0 and result <= len(types)-1 else result), end='\n')
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
        else:
            print(result)

    except ValueError:
        print('No ha seleccionado una opción valida:\n')

        # exit = input(
        #     'Opcion invalida\nPara abandonar el proceso oprima la tecla S: ')
        # if exit.upper() == 'S':
        #     break

# if exit == 'S':
#     print('El proceso finalizó de forma interrumpida por el usuario,\nGracias.')
# else:

#     if CRUD[choiceCrud] == CRUD[1]:
#         print('Felicidades, ha agregado un nuevo tipo con éxito\n')
#     else:
#         exit()
#         print('Confirmación\nHa eliminado el tipo: {0}\nDel listado de tipos:'.format(
#             types.pop(result)), end='\n')

#     print('\nLista de tipos actualizada: ', end='\n[ ')
#     i = 0
#     for tipo in types:
#         print('{0}-{1}'.format(i, tipo), end=' ░ ' if i < len(types)-1 else '')
#         i += 1
#     print(' ]')
