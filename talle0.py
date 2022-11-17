# TALLER PYTHON - N°1

# Autor: Julián Rodriguez
# Fecha: Nov-11-2022

from datetime import date
from datetime import datetime

today = date.today()  # Fecha actual
start = datetime.now()  # Fecha actual
print('Bienvenido \n Hoy es el día: ', today)
print('---------------')

valores = []
n0 = float(input('Ingrese un número: '))
n1 = float(input('Ingrese un número: '))
valores.append([n0, n1])
print('Valores ingresados =', valores)
print('---------------')


print('la suma de ', n0, 'y', n1, ' = ', n0 + n1)
print('---------------')

total = n0 - n1
print('la resta de ', n0, 'y', n1, ' = ', total)
print('---------------')

total = n0 * n1
print('la multiplicacion de %f y %f = %f' % (n0, n1, total))
print('---------------')

total = n0 / n1
print('la división de %.2f y %.2f = %.4f' % (n0, n1, total))
print('---------------')

end = datetime.now()  # Fecha actual
print('Duración de la ejecución = ', end - start)
