# concatenacion / Comentarios

numero0 = 10
numero1 = 20

string0 = 'VENDEDOR 1'
string1 = 'VENDEDOR 2'

list0 = ['1', '2', '20', '15', '5']
list1 = ['2', '6', '10', '12', '10']

tupl0 = ('CANNABIS', 'COCAINA', 'WAKS')
tupl1 = ('CANNBIS', '2CBD', 'CRACK')

# Concatenar con +
# SOLO PERMITE CONCATENAR CON + CUANDO SON DEL MISMO TIPO

print(numero0 + numero1)  # 30
print(string0 + ' / ' + string1)  # VENDEDOR 1 VENDEDOR 2
print(list0 + list1)  # ['1', '2', '20', '15', '5', '2', '6', '10', '12', '10']
print(tupl0 + tupl1)  # ('CANNABIS', 'COCAINA', 'WAKS', 'CANNBIS', '2CBD', 'CRACK')


# Concatenar con ,
# SOLO PERMITE CONCATENAR ENTRE TIPOS DE DATOS
print(string0, numero0)  # 'VENDEDOR 1' 10
print(string0, list0)  # VENDEDOR 1 ['1', '2', '20', '15', '5']
print(string0, tupl0)  # VENDEDOR 1 ('CANNABIS', 'COCAINA', 'WAKS')
