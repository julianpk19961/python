# Trabajo con colecciones de valores LISTAS

CRUD = ['Salir', 'Crear', 'Leer', 'Actualizar', 'Eliminar']
ans = ['NO', 'SI']
types = ['Bicho', 'Dragón', 'Eléctrico', 'Hada', 'Lucha', 'Fuego', 'Volador', 'Fantasma',
         'Planta', 'Tierra', 'Hielo', 'Normal', 'Veneno', 'Psíquico', 'Roca', 'Acero', 'Agua']

i = 0
for tipo in types:
    print('{0} - {1}'.format(i, tipo))
    i += 1

print()

i = 0
for option in CRUD:
    if i == 0:
        print('S - {0}'.format(option))
    else:
        print('{0} - {1}'.format(i, option))
    i += 1

# Elección del tipo de acción que será ejecutada
exit = ''

while True:
    choiceCrud = input('Ingrese la opción que desea realizar: ')

    try:

        if choiceCrud.upper() == 'S':
            exit = choiceCrud
            break

        choiceCrud = int(choiceCrud)

        if choiceCrud >= 0 and choiceCrud <= len(CRUD):
            if (choiceCrud > 0):
                break
            else:
                exit()

    except ValueError:
        print('Opción invalida\n')

if exit.upper() != 'S':

    # print('\nPara {0} un tipo de pokemon escriba'.format(CRUD[choiceCrud]))

    result = ''
    confirmation = ''

    # Procedimiento
    while True:

        if exit.upper() == 'S' or (result != '' and confirmation == 1):
            break

        if CRUD[choiceCrud] == CRUD[1]:
            msg = 'Ingrese el nombre del tipo que desea crear: '

        else:
            msg = 'Ingrese el valor del listado de 0 a {0}: '.format(
                len(types)-1)

        try:
            result = input(msg)

            result = int(result) if (len(result) <= 2 and result !=
                                     'S' and choiceCrud != 1) else result

            if type(result) != int and result.upper() == 'S':
                exit = result
                break

            print('¿Esta seguro de {0} el tipo: {1}'.format(CRUD[choiceCrud],
                                                            types[result] if type(result) == int else result), end='\n')

            y = 0
            for choiseans in ans:
                print('{0}-{1}'.format(y, choiseans), end='\t')
                y += 1

            while True:
                confirmation = input('\nDígite la respuesta: ')

                try:
                    confirmation = int(confirmation)

                    if confirmation in [0, 1]:
                        exit = 'S' if confirmation == 0 else ''
                        break

                    else:
                        print('Opción invalida\n')

                except ValueError:
                    print('Opción invalida\n')

            break

        except ValueError:
            print('No ha seleccionado una opción valida:\n')


if exit.upper() == 'S':
    print('El proceso finalizó de forma interrumpida por el usuario,\nGracias.')
else:

    if choiceCrud == 1:

        print(
            '¿Desea indicar la posición donde será ubicado el nuevo tipo: {0}?'.format(result))

        y = 0
        for choiseans in ans:
            print('{0}-{1}'.format(y, choiseans), end='\t')
            y += 1

        while True:
            addConfirmation = input('\nDígite la respuesta: ')
            try:
                addConfirmation = int(addConfirmation)

                if addConfirmation in [0, 1]:
                    break
                else:
                    print('Opción invalida\n')

            except ValueError:
                print('No ha seleccionado una opción valida:\n')

        if addConfirmation == 1:
            position = input(
                'Por favor ingrese el número de la posición, posición valida desde la N° 0 a la {0}:\t'.format(len(types)))

            if position.upper() == 'S':
                pass

            while True:
                position = int(position)

                try:
                    if position >= 0 and position <= len(types)-1:
                        types.insert(position, result)
                        break
                except ValueError:
                    print('Opción invalida.\n')
        else:
            types.append(result)
    if choiceCrud == 4:
        del (types[result])


if exit.upper() != 'S':

    # types.sort() -> ordenar ascendente
    # types.sort('key') -> ordenar por clave
    # types.sort(reverese='True) -> ordenar ascendente

    print('\nLista de tipos actualizada: ', end='\n[ ')
    i = 0
    for tipo in types:
        print('{0}'.format(tipo), end=' ░ ' if i < len(types)-1 else '')
        i += 1
    print(' ]')

    print('\nTotal de tipos encontrados: ', len(types))
    # print(types.sort(reverse=True))
