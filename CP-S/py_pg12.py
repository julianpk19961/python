# Condicionales Simples

# IF & IF ELSE

a = float(input('IF: Ingrese el número a evaluar: '))

# Para que el valor aplique solo al condicional debe haber una identación:
if a < 0:
    tipo = 'negativo'

if a > 0:
    tipo = 'positivo'

if a == 0:
    tipo = 'ninguno'

# Condicional con else [multiple]
if a != 0:
    if a % 2 == 0:
        categoria = 'par'

    if a % 2 != 0:
        categoria = 'impar'

if a == 0:
    categoria = 'ninguna'

print('VALOR INGRESADO: %.0f \nTIPO: %s \nCATEGORIA: %s' % (a, tipo, categoria))


# El uso de else es opcional. Si no se coloca, nada sucederá cuando la condición sea ‘Falsa’.
# Si por algún motivo no se quisiera ejecutar instrucción alguna en uno de los bloques,
# se debe usar la instrucción pass (esta orden significa que no tiene que hacer nada).

a = float(input('ELIF: Ingrese el número a evaluar: '))

if a < 0:
    tipo = 'negativo'
elif a > 0:
    tipo = 'positivo'
elif a == 0:
    tipo = 'ninguno'
else:
    pass

# Condicional con else [multiple]
if a != 0:
    if a % 2 == 0:
        categoria = 'par'

    elif a % 2 != 0:
        categoria = 'impar'
else:
    categoria = 'ninguna'
print('VALOR INGRESADO: %.0f \nTIPO: %s \nCATEGORIA: %s' % (a, tipo, categoria))
