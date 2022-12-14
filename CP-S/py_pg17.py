# CICLO WHILE

# Permite repetir la ejecución de un bloque de instrucciones mientras se cumpla
# una condición, es decir, mientras la condición tenga el valor TRUE


# Estructura WHILE

# while condicion:
#     cuerpo del bucle

clases = {'Bicho', 'Dragón', 'Eléctrico', 'Hada', 'Lucha', 'Fuego', 'Volador', 'Fantasma',
          'Planta', 'Tierra', 'Hielo', 'Normal', 'Veneno', 'Psíquico', 'Roca', 'Acero', 'Agua'}
initials = ['Bulbasaur', 'Squirtle', 'Charmander']

attempts, maxAttempts = 1, 10

top = 50


i = len(clases)

choise = int(input(
    "¿Adivina cuantas clases de pokemon hay? inserta un número del 0 al %s :" % (top)))

if choise > top:
    print('El número no es valido')
    quit()

while choise != i:
    attempts += 1
    if attempts < maxAttempts:
        choise = int(input(
            "¿Adivina cuantas clases de pokemon hay? inserta un número del 0 al %s :" % (top)))
    else:
        print('Lo sentimos ha superado el limite permitido de intentos')
        quit()

print('¡Felicidades, has acertado!\nson %s clases de pokemón\nNúmero de Intentos: %s ' % (i, attempts))


