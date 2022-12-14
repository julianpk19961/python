# Estructuras de control condicionales
# (tambien llamados logicos)
# Python cuenta con 3 operadoras: and , or y not

# AND   = TRUE cuando todas sus condiciones se cumplen
# OR    = TRUE cuando una de sus condiciones se cumplen, solo es FALSE
#           Cuando todas sus condiciones son FALSE.
# NOT   = TRUE cuando el operador es FALSE y viceversa ES UNITARIO


# ORDEN DE PRIORIDAD OPERADORES
# NOT->AND->OR

# ELEMENTOS NULL o EMPTY = FALSE, LOS DEMAS SON TRUE

# NULL
print('NULL = ', bool())

# EMPTY 
a = ''
print('EMPTY = ', bool(a))
# TABLA

a = b = 2
print('a =', a)
print('b =', a)
# -AND
# True  AND True    = True
# False AND True    = False
# True  AND False   = False
# False AND False   = False
print('---AND---')
print('[(a = 2) AND (b = 2)] = TRUE')
print('[(a = 1) AND (b = 2)] = FALSE')
print('[(a = 2) AND (b = 1)] = FALSE')
print('[(a = 1) AND (b = 1)] = FALSE')


# -OR
# True  OR True    = True
# False OR True    = True
# True  OR False   = True
# False OR False   = False
print('---OR---')
print('[(a = 2) OR (b = 2)] = TRUE')
print('[(a = 1) OR (b = 2)] = TRUE')
print('[(a = 2) OR (b = 1)] = TRUE')
print('[(a = 1) OR (b = 1)] = FALSE')

# -NOT
# True  = False
# False = True
print('---NOT---')
print('NOT( a = 2 ) = FALSE')
print('NOT( a = 1 ) = TRUE')
