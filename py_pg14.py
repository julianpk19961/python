# Uso de ELIF
# Existen también las llamadas Condicionales encadenadas.
#  A veces hay más de dos posibilidades y necesitamos más de dos ramificaciones.
# Una forma de expresarlo es con una condicional encadenada,
# donde solo se puede cumplir una de las ramificaciones o ninguna de ellas.

# La sentencia elif es una abreviatura de “else if ”.
# No existe un límite definido al uso de sentencias elif,
# pero solo se permite una sentencia else (que es opcional) y debe ser la última rama de la sentencia:
# Ejemplo:
# if condición1:
#     bloque de instrucciones para ‘Verdadero’ a la condición1

# elif condición2:
#     bloque de instrucciones para ‘Verdadero’ a la condición2

# elif condición3:
#     bloque de instrucciones para ‘Verdadero’ a la condición3

# else:
#     hacer esto solo para ‘Falso’ a todas las condiciones anteriores
#     bloque de instrucciones

# Siguiente instrucción después de la condicional
# bloque de instrucciones

choise = int(input(
    'Ingrese el número del cantidato que desea elegir:\n(1) - Andrés\n(2) - Julián \n(3) - Susan: \n Digite aquí su voto: '))

if choise == 1:
    candidato = 'Andrés'
elif choise == 2:
    candidato = 'Julián'
elif choise == 3:
    candidato = 'Susan'
else:
    candidato = 'NO VALIDO'

print('¡VOTO REGISTRADO PARA:', candidato, '!')
print('Gracias por participar')
