# Taller 5: Python
# Autor: Julian Rodriguez
# Fecha:11-Dic-2022

from datetime import date
from datetime import datetime
import sys

today = date.today()
now = datetime.now()
version = sys.version_info.major

current_time = now.strftime("%H:%M:%S")

print('\BIENVENIDO\n---')
print('FECHA:\t', today)
print('HORA:\t', current_time)
print('VERSION:\t', version)

nombre = input('Ingrese su nombre: ')
for char in nombre:
    print(char.upper(),end=' ')
print('\n')

ciclos = ['Range(i)', 'Range(i,f)', 'Range(i,f,inc)']
i = 0

for ciclo in ciclos:
    print('Escriba: [%d] si desea estudiar: %s' % (i, ciclo))
    i += 1

while True:
    choise = input('Ingrese una opción valida: ')
    try:
        choise = int(choise)
        if choise <= len(ciclos)-1:
            break
    except ValueError:
        print('¡Ops, al parecer la opción ingresada no es valida!')


if choise >= 0:
    nombreValor = 'rango' if choise == 0 else 'rango inicial'
    while True:
        i = input('Ingrese el valor de el %s: ' % (nombreValor))
        try:
            i = int(i)
            break
        except ValueError:
            print('¡Ops, al parecer la entrada es incorrecta')

if choise >= 1:
    while True:
        f = input('Ingrese el valor del final del rango: ')
        try:
            f = int(f)
            break
        except ValueError:
            print('¡Ops, al parecer la entrada es incorrecta')


if choise == 2:
    while True:
        inc = input('Ingrese el valor del incremento: ')
        try:
            inc = int(inc)
            break
        except ValueError:
            print('¡Ops, al parecer la entrada es incorrecta')

if choise == 0:
    f, i, inc = i, 0, 1
    i_auto, f_auto, inc_auto = 1, 0, 1

elif choise == 1:
    i_auto = f_auto = 0
    inc = inc_auto = 1

else:
    i_auto = f_auto = inc_auto = 0

print('\nDESDE: %d\tAUTOMATICO->[%s]' %
      (i, 'SI' if i_auto == 1 else 'NO'))
print('HASTA: %d\tAUTOMATICO->[%s]' %
      (f, 'SI' if f_auto == 1 else 'NO'))
print('INCREMENTO: %d\tAUTOMATICO->[%s]\n' %
      (inc, 'SI' if inc_auto == 1 else 'NO'))

print('\n ARRAY GENERADO CON CICLO FOR:')
print('[ ',end='')
for n in range(i, f, inc):
    print('%d' % (n), end=" ")
print(']')
print('---FIN---')