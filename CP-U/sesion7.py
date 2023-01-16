# Introducción a tuplas

types = ('Bicho', 'Dragón', 'Eléctrico', 'Hada', 'Lucha', 'Fuego', 'Volador', 'Fantasma',
         'Planta', 'Tierra', 'Hielo', 'Normal', 'Veneno', 'Psíquico', 'Roca', 'Acero', 'Agua')

# Mostrar Conjunto
print(types)
# longitud
print(len(types))
# mostrar posición
print(types[5])

# convertir tupla a lista
# types_list = list(types)
# print(types_list)

# convertir lista a tupla
# types_newTuple = tuple(types_list)
# print(types_newTuple)

# convertir tupla a listado

len_total = len(types)

while True:

    choise = int(input(
        'Para seleccionar un tipo ingrese una opción entre 0 y %s: ' % format(len_total)))
    try:

        if (choise > len_total or len_total < 0):
            print('Opción invalida \n')
        else:
            break
    except ValueError:
        print('Parece que algo salió mal \n')

print('Ha elegido el tipo: ', types[choise])

tipo = input('Digite el nombre del tipo que desea comprobar: ')

if tipo.title() in types:
    print('El tipo ingresado existe!')
else:
    print('Lo sentimos, ese tipo de pokemón aún no ha sido registrado en la pokedex!')
