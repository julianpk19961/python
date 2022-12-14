# 3.6 Librería: Random
# ->Requiere ser importada de la librería 'random'.
import random

# ->random.randint(a,b)
#      a=inicio , b=fin
x = random.randint(1, 10)
print('random.randint(1,10) = ', x)

# ->random.randrange(a,b,c)
#      a = inicio , b = fin , c = incremento
x = random.randrange(0, 50, 5)
print('random.randrange(0,50,5) = ', x)

# ->random.random()
#      Numero aleatorio entre 0.0 y 1.0
print('random.random() = ', random.random())

# ->random.uniform(a,b)
#      a=inicio , b = fin
#     Numero aleatorio entre 100.0 y 200.0
x = random.uniform(100, 200)
print('random.uniform(100,200) = ', x)

# ->random.choise(a)
#      a = lista de elementos
#     seleccionar al azar un dato desde un conjunto
amigos = ['Julian', 'Andres', 'Heiner', 'Daniel']
print('random.choice(', amigos, ')= ', random.choice(amigos))


# ->random.shuffle(a)
#      a = lista de valores
#     Modifica el orden de los elementos de una lista random.shuffle() dentro de la misma variable[el contenido original es cambiado].
naipes = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
print(naipes)
random.shuffle(naipes)
print(naipes)

# ->random.sample(a,b)
#      a = lista elementos , b = cantidadmuestra
#     Para reorganizarlos elementos puede usar la función sample tomando como muestra todos los elementos.
print('random.sample(', naipes, ',len(', naipes, ')) = ',
      random.sample(naipes, len(naipes)))

#     extrae una cantidad de numeros aleatorios del conjunto
random.sample(naipes, 3)  # se tomaron 3 cartas del total de naipes al azar
print(random.sample(naipes,3))

# ->random.sorted(a,key)
#      a = lista elementos , llave por la cual será ordenada el listado deno ser indicado se hará de forma acendente
#     Tambien es posible usar sorted() con random.random para reordenar una lista generando una lista nueva.
print(sorted(naipes, key=lambda k: random.random()))
