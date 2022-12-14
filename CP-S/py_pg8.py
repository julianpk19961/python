# Librerías matemáticas
# requieren ser importadas de la librería math.

import math

# vars
a = 1000
b = 500.30
c = 22
angulo = 60
radianes =  math.radians(angulo)


# ->trunc(n)
#   Elimina los decimales de un número float
print('math.trunc(', b, ') = ', math.trunc(b))

# ->fabs(n)
#   Calcula el valor absoluto de número float eliminando el signo
print('math.fabs(', b, ') = ', math.fabs(b))

# ->factorial(n)
#   Calcula el número de combinaciones posibles de una serie de objetos. [ (n!) representación marematica]
#   Solo aplica para números enteros.
print('math.factorial(', c, ')= ', math.factorial(c))

# ->fmod()
#   Calcula el residuo de una división entre dos float
print('math.fmod(',a,',',b,') =', math.fmod(a,b))

# ->sqrt()
#   Calcula la raiz cuadrada
print('math.sqrt(', a, ')= ', math.sqrt(a))


# ======
# -> Las funciones trigonométricas en la librería math toman los valores de los ángulos expresados como radianes.
#       Por esta razón, debe realizarse la conversión de grados a radianes con la función radians.
# -> Las funciones trigonométricas seno, coseno y tangente se realizan usando sin(), cos() y tan().
# ======

# ->radians(a)
#   a = número
print('math.radians(', angulo, ')= ', radianes )

# ->Las funciones trigonométricas seno, coseno y tangente se realizan usando:
#   sin(), cos() y tan().
print( 'math.sin(', radianes ,')' ,math.sin(radianes))
print( 'math.cos(', radianes ,')' ,math.cos(radianes))
print( 'math.tan(', radianes ,')' ,math.tan(radianes))