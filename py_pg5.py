# 3.5 Funciones predefinidas de Python


# len() calcula la logintud de caracteres de una cadena
x = 'Hola mundo'
# print('\nlen("', x,'") = ', len(x))

# split() convierte una cadena en una lista
x = "Bienvenidos al curso de variables y tipos de datos en python"
# print( '\n(', x ,').split() = ', x.split() )

# lower() convierte una cadena en minúscula
x = 'MIRA COMO ME HAGO PEQUEÑO'
# print( '\n(', x ,').lower() = ', x.lower() )

x = 'mira como me hago grande'
# print('\n(',x,').upper() = ',x.upper())

# replace() reeplaza una cadena por otra
x = 'PHP es un gran lenguaje'
# print('\n(', x, ').replace("PHP","PYTHON") = ', x.replace(
#     'PHP', 'PYTHON'))

# list() Crea una lista a partir de un elemento
x = range(4)
# print('\n list(', x, ') = ', list(x))

# range(n) Crea un rango de números n=numero del rango
x = range(6)
# print('\n range(6) = ', list(x))


# str() convierte un valor númerico a texto
x = 100
# print('\n str("100") = ', str(x))


# int() Convierte valor entero
x = "20"
# print('\n str("20") = ', int(x))

# float() Convierte el valor a decimal
x = 5
# print('\n float(5) = ', float(x))


# max() Determina el máximo entre un grupo de números
x = [1, 4, 5, 10]
# print('\n max([1, 4, 5, 10]) = ', max(x))


# min() Determina el máximo entre un grupo de números
x = [1, 4, 5, 10]
# print('\n min([1, 4, 5, 10]) = ', min(x))


# sum() Determina el máximo entre un grupo de números
x = [1, 4, 5, 10]
# print('\n sum([1, 4, 5, 10]) = ', sum(x))


# ord() Devuelve el valor ASCII de una cadena o caracter
x = '@'
# print('\n ord(@) = ', ord(x))

# round() Redondea después de la coma de un float
x = 16.92
y = 16.42
# print('ROUND(',x,') = ', round(x))
# print('ROUND(',y,') = ', round(y))
