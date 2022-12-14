# 2.3 Impresión de cadenas

#Las cadenas tienen varias formas de ser impresas en pantalla. Veamos el siguiente cuadro:

frase1= 'Bienvenidos '
frase2= 'este es su curso de variables en python, '
frase3= 'aquí inicia su camino'


# NOTACION              USO                         
# +                     Concatena Cadenas  
show = frase1 + frase2 + frase3 # Bienvenidos Este es su curso de variables en python Aquí inicia su camino.
print(show)

# *                     Repite Cadenas  
show = string0 = frase1 * 3 #BienvenidosBienvenidosBienvenidos
print(show)

# cadena.capitalize()   Inicia con mayúscula    
show = frase3.capitalize() #Aquí inicia su camino
print(show)

# cadena.center(n)      Centra en el ancho dado (n)
show = frase1.center(18) #" Bienvenidos "   
print(show)

# cadena.lower          Pasa todo a minúscula
show = frase1.lower() #" bienvenidos "   
print(show)

# cadena.upper          Pasa todo a mayúscula 
show = frase1.upper() #" BIENVENIDOS "   
print(show)

# cadena.title          Mayúsculas Iniciales
show = frase3.title() #" Aquí Inicia Su Camino "   
print(show)
