# 3.6 Librerías de fecha, random y matemáticas

# Si se necesita usar fechas en un programa, es necesario importar las librerías Python: datetime y date

from datetime import date
from datetime import datetime
import random


today = date.today()
# print('date.today() = ', today)

nowIs = datetime.now()
# print('datetime.now() = ',nowIs)


# Librerías random

# Numero aleatorio entre 1 y 10
x = random.randint(1, 10)
# print('random.randint(1,10) = ',x)

# Numero aleatorio entre 0 y 50 con incrementos de 5
x = random.randrange(0, 50, 5)
# print('random.randrange(0,50,5) = ', x)

# Numero aleatorio entre 0.0 y 1.0
x = random.random()
# print('random.random() = ',x)

# Numero aleatorio entre 100.0 y 200.0
x = random.uniform(100, 200)
print('random.uniform(100,200) = ', x)

# CHOISE
# seleccionar al azar un dato desde un conjunto
amigos = ['Luis', 'Mauricio', 'Patricia', 'Carlos']
# print('amigos: ',amigos)
ganador = random.choice(amigos)
# print('El ganador fue: ',ganador)

# Shuffle
# Modifica el orden de los elementos de una lista
naipes = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
print('naipes: ', naipes)
random.shuffle(naipes)  # los naipes se barajaron al azar
print(naipes)

# SAMPLE
# extrae una cantidad de numeros aleatorios del conjunto
random.sample(naipes, 3)  # se tomaron 3 cartas del total de naipes
print(random.sample(naipes, 3))
