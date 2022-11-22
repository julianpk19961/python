# Condicionales Simples
a = float(input('Ingrese el número a evaluar: '))


# Para que el valor aplique solo al condicional debe haber una identación:
if a < 0:
    tipo = 'negativo'

if a > 0:
    tipo = 'positivo'

if a == 0:
    tipo = 'ninguno'

#Condicional con else [multiple]
if a != 0:
    if a % 2 == 0:
        categoria = 'par'
    else:
        categoria = 'impar'
else:
    categoria = 'ninguna'


print('VALOR INGRESADO: %.0f \nTIPO: %s \nCATEGORIA: %s' % (a, tipo, categoria))
