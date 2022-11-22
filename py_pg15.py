# Expresiones booleanas compuestas:

# es posible tener más de una expresión booleana en la misma sentencia condicional.
# A esto se le llaman expresiones booleanas compuestas.
# Un ejemplo: hallar el número más pequeño entre tres números enteros.

# Se observa que el primer test es una expresión booleana compuesta.
# Todos los operandos tienen que ser ciertos para que la siguiente instrucción se ejecute.


# C2 = a2 + b2
#

a = int(input('ingrese el valor númerico de a:\n'))
b = int(input('ingrese el valor númerico de b:\n'))
c = int(input('ingrese el valor númerico de c:\n'))
print('----------------------------------')

if a < b and a < c:
    lownumber = a
elif b < a and b < c:
    lownumber = b
elif c < b and c < b:
    lownumber = c

if a > b and a > c:
    highnumber = a
elif b < a and b < c:
    highnumber = b
elif c < b and c < b:
    highnumber = c


print('Numeros ingresados: %d , %d, %d' % (a, b, c))
print('----------------------------------')

print('Número más alto:', highnumber)
print('Numero más bajo:', lownumber)
