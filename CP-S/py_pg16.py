# Ciclos iterativos con Python
# Pueden ser
# ciclos fijos: Predefinidos por el desarrollador.
# ciclos variables: Predefinidos depeden de el usuario o parametros especificos.

# DENTRO DE LOS CICLOS ESTÁN:
# FOR Y WHILE
# SE USA DEPENDIENDO DE LA NECECIDAD DEL DESARROLLADOR O PROBLEMA


# FOR
# USAR CUANDO HAY CLARIDAD EN LA CANTIDAD DE VECES QUE SE DEBE EJECUTAR UN BLOQUE

# EJ:
# SUMAR UN SEGUNDO HASTA LLEGAR A 60
# SUMAR UN MINUTO HASTA LLEGAR A 60
# SUMAR UNA HORA HASTA LLEGAR A 24

initials = ['Bulbasaur', 'Squirtle', 'Charmander']
print('Pokedex')

print('CICLO FOR')
for pokemon in initials:
    print('Pokemon:{0} Tamaño del nombre es de:\t {1}'.format(
        pokemon, len(pokemon)))
print('------\n')

print('El ciclo inicia en 0 cuando solo se ingresa un valor')
print('CICLO FOR + RANGE(10)')
for i in range(10):
    continue
    print('i=', i)
print('------\n')

print('El ciclo aumenta o disminuye en 1 implicitamente si no se especifica\nun valor de aumento\decremento')
print('CICLO FOR + RANGE(50, 0, -4)')
for i in range(50, 0, -4):
    continue
    print('i =', i)
print('------\n')

print('Ciclo FOR en cadenas')
for pokemon in initials[0]:
    continue
    print(pokemon)
print('------\n')

print('Ciclo FOR en cadenas')
for pokemon in initials[0]:
    continue
    print(pokemon)
print('------\n')

print('Ciclo FOR en tuplas')
conexion_db = ('192.1.1.0', 'root', '3360', 'pokedex')

for parametro in conexion_db:
    continue
    print(parametro)
print('------\n')

print('Ciclo FOR en conjuntos')
print('\nTabla de tipos')
clases = {'Bicho', 'Dragón', 'Eléctrico', 'Hada', 'Lucha', 'Fuego', 'Volador', 'Fantasma',
          'Planta', 'Tierra', 'Hielo', 'Normal', 'Veneno', 'Psíquico', 'Roca', 'Acero', 'Agua'}
for clase in clases:
    if clase == "Planta":
        clase += ' LA MEJOR DE TODAS'
    if clase == 'Normal':
        continue
    print(clase)
print('------\n')
