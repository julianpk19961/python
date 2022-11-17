#Introducción

# Dialogo para interactuar con el usuario.
print("Hola, este es el curso de 'Variables y estructuras de control en python'")

# Dialogo con captura de datos [todos los datos capturados si no son transformados luego serán str]
fullname = input('ingrese su nombre completo ')
borndate = int(input('ingrese su año de nacimiento '))
age = 2022 - borndate

# Para concatenar datos en una impresión usar ','
print('Hola', fullname, '. Según su año de nacimiento ingresado (',
      borndate, ') uste tiene: ', age, ' años')
