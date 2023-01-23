# Ciclo cor
title = 'months'

print('BIENVENIDO\n')
while True:
    x = input('¿De que número desea realizar la tabla de multiplicar?\t')
    try:
        x = int(x)
        break
    except ValueError:
        print('Lo sentimos, no ha ingresadon una opción valida\nIntente nuevamente, por favor:\n')

for i in range(1, -12, -1):
    print('%.2f x %.2f = %.2f' % (i, x, i*x))

print('\n', title.upper(), '\n')
months = ['January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October', 'November', 'December']
print('List:', end='')
print(months)
print('\n', title.upper(), '\n')
print('\nMONTHS\n')
for month in months:

    if month == 'January':
        pass
    if month == 'March':
        continue
    if month == 'October':
        break
    print('idioma: %s' % (month))
