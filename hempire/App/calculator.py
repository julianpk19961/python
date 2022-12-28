print('Bienvenido a "Hempire Calculator"')

# diccionario = {'edad': 22, 'ciudad': 'Bello', 'lista': lista, 'tupla': tupla}
# tupla = ('Colombia', '2022', 3333, 'Argentina', 'Chile')
# lista = ['ELEMENTO 0', 1, -2.5, '333333', 'elemento 4']

categories = [
    {'id': 0, 'name': 'Indica'},
    {'id': 1, 'name': 'Hybrid'},
    {'id': 2, 'name': 'Sativa'}
]

strains = [
    {'id': 0, 'name': 'Afghani', 'category': 0},
    {'id': 1, 'name': 'Northern Lights', 'category': 0},
    {'id': 2, 'name': 'Hindu Kush', 'category': 0},
    {'id': 3, 'name': 'Stunk #1', 'category': 1},
    {'id': 4, 'name': 'Chemdawg', 'category': 1},
    {'id': 5, 'name': 'G13 Haze', 'category': 1},
    {'id': 6, 'name': 'Sour Diesel', 'category': 2},
    {'id': 7, 'name': 'Haze', 'category': 2},
    {'id': 8, 'name': 'Jack Herer', 'category': 2}
]

strainMaestries = [
    {'id': 0, 'level': 1},
    {'id': 1, 'level': 2},
    {'id': 2, 'level': 3},
    {'id': 3, 'level': 4},
    {'id': 4, 'level': 5},
    {'id': 5, 'level': 6},
    {'id': 6, 'level': 7}
]

pots = [
    {'id': 0, 'name': 'normal', 'timeAceleration': 0},
    {'id': 1, 'name': 'magic', 'timeAceleration': 0.5}
]


print(categories, end='\n')
print(strains, end='\n')
print(strainMaestries, end='\n')
print(pots)
