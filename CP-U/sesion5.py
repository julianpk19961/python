# Trabajo con metodos númericos.
a = int(input('Ingrese el valor del primer número: '))

b = int(input('Ingrese el valor del segundo número: '))


# SUMA
print('%d + %d = %d' % (a, b, a+b))
# RESTA
print('%d - %d = %d' % (a, b, a-b))
# MULTIPLICACION
print('%d * %d = %d' % (a, b, a*b))
# DIVISION
print('%d / %d = %d' % (a, b, a/b))

# Potencia
print("%d^%s = %d" % (a, b, a ** b))

# RESIDUO
print('%d %s %d = %d' % (a, '%', b, a % b))

# Trabajo con float
a = float(round(a/100, 2))
b = float(round(b/100, 2))
c = a * b
c *= -1
print('a = %.2f' % (a))
print('b = %.2f' % (b))
print('(a*b)(-1) = %.2f' % (c))
