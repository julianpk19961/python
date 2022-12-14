# TALLER PYTHON - N°2
# Autor: Julián Rodriguez
# Fecha: Nov-29-2022

from datetime import date
from datetime import datetime

hoy = date.today()
hora = datetime.now()
print('BIENVENIDO\nHoy es el día:', hoy,
      '\nHora local:', hora.strftime("%H:%M:%S"))
print('----------------------------------')
a = int(input('digite el primer número:\t'))
b = int(input('digite el segundo número:\t'))
c = int(input('digite el tercero número:\t'))

x = [a, b, c]

print('\nEl valor máximo es: ', max(x))
print('El valor mínimo es: ', min(x))
print('La suma de los valores ingresados es: ', sum(x))

print('\n----------------------------------')
f = float(input('Digite un número con decimales: '))
print('El valor redondeado de ', f, ' es:', round(f))

print('\n----------------------------------')
s = input('Digite una oración: ')
print('Mayúscula: ', s.upper())
print('Minúscula: ', s.lower())
print('Primera letra mayúscula: ', s.capitalize())
print('Primera letra de cada palabra en mayúscula: ', s.title())
print('El tamaño de la frase ingresada fue de: ', len(s))
print('----------------------------------\nGRACIAS, VUELVA PRONTO')
