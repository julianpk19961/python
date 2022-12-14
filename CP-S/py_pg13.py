# Condicionales anidadas

# En algunas ocasiones se requiere que después de una condicional se incluya una segunda condicional
# o quizás una tercera condicional. A continuación se detallará la sintaxis para codificar varias condicionales
# anidadas en un solo bloque.

# if (condicion):
#     hacer esto solo para ´verdadero
#     bloque de instruccion
# else:
#     hacerto solo para 'falso'
#     bloque de instruccione

curso0 = input('Ingrese el nombre del curso: ')
curso1 = input('Ingrese el nombre del curso: ')

print('\nEl primer curso ingresado es: %s' % (curso0))
print('El segundo curso ingresado es: %s' % (curso1))

if curso0 == 'Requerimientos' or curso0 == 'Algoritmos':
    if curso1 == 'Algoritmos' or curso1 == 'Requerimientos':
        print('Bienvenido Programador')

    else:
        if curso0 == 'Requerimientos':
            cursoTomar = 'Algoritmos'
        else:
            cursoTomar = 'Requerimientos'

        print('\nSi quiere continuar el camino a gran programador \nLe recomendamos tomar el curso de: %s' % (cursoTomar))
else:
    print('\nUsted no es programador')

print('------------')
