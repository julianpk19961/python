# 2.2 Salida de datos con formato

# Python es compatible con la salida de datos con formato. El caracter módulo % es un operador integrado en Python.
# Este es conocido como el operador de interpolación.
# Se deben digitar los formatos deseados, el signo % (porcentaje), seguido por paréntesis con los datos que necesitan ser convertidos.
# La sintaxis de la instrucción es:
#   print (“cadena con formato” % (variables separadas por comas))

# Se utilizan los siguientes formatos para la salida de datos:
    # %c = un caracter
    # %s = str, cadena de caracteres
    # %d = int, enteros
    # %f = float, flotantes 
    #       -> para imprimir con un tamaño exacto de decimales es %.nf donde n es el número de decimales

#Ejemplo

titulo = "Programa número 3"
dia = 16
mes = 11
anio = 2022
tmp = 6.3
pi = 3.1416

print ('Bienvenido al: %s hoy es: %d / %d / %d y estamos a %.2f °C - \n el valor de π = %f' % (titulo , dia,mes,anio,tmp,pi) )