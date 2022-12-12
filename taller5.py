# Taller 6: Python
# Autor: Julian Rodriguez
# Fecha:12-Dic-2022


from datetime import datetime
now = datetime.now()
options = ['CONTROLADOR', 'EVENTO', 'CON BREAK']
y = 0


print('BIENVENIDO\n')
print('FECHA ACTUAL:\t', now.date())
print('HORA ACTUAL:\t', now.timetz())
print('------\n')

print('TALLER 6 CICLOS ITERATIVOS: WHILE\n')

for option in options:
    print('DIGITA: %s PARA SELECCIONAR: %s' % (y, option))
    y += 1
y = 0

while True:
    choiseOption = input('OPCIÓN SELECCIONADA: ')
    try:
        choiseOption = int(choiseOption)
        if choiseOption >= 0 and choiseOption <= len(options)-1:
            break
    except ValueError:
        print('OPCION INVALIDA INTENTE DE NUEVO:\n')

print('\n')
for character in options[choiseOption]:
    print(character)
print('\n')

if choiseOption >= 0:
    while True:
        messagge = 'limite' if choiseOption == 0 else 'inicio'
        i = input('Ingrese el valor del %s: ' % (messagge))
        try:
            i = int(i)
            if choiseOption == 0:
                f = i
                i = 0
            break
        except ValueError:
            ('Valor ingresado no valido, intente de nuevo: ')

if choiseOption >= 1:
    while True:
        f = input('Ingrese el valor del limite: ')
        try:
            f = int(f)
            break
        except ValueError:
            ('Valor ingresado no valido, intente de nuevo: ')

if choiseOption == 2:
    while True:
        b = input('Ingrese el valor de salida: ')
        try:
            b = int(b)
            if b <= f:
                break
        except ValueError:
            ('Valor ingresado no valido, intente de nuevo: ')

print('------')
print('\nINICIO:%d\nFINAL:%d' % (i, f))
if 'b' in locals():
    print('SALIDA: %d' % (b))

y = i
while y <= f:
    print(y)
    y += 1
    if 'b' in locals() and y == b:
        print('SALIDA CON BREAK\n')
        break

print('FIN DEL CICLO')
