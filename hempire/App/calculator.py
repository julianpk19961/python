print('Bienvenido a "Hempire Calculator"')

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
    {'id': 8, 'name': 'Jack Herer', 'category': 1},
    {'id': 9, 'name': 'none', 'category': ''},
]

strainMaestries = [
    {'id': 0, 'level': 1, 'buds': 1},
    {'id': 1, 'level': 2, 'buds': 2},
    {'id': 2, 'level': 3, 'buds': 3},
    {'id': 3, 'level': 4, 'buds': 4},
    {'id': 4, 'level': 5, 'buds': 5},
    {'id': 5, 'level': 6, 'buds': 6},
    {'id': 6, 'level': 7, 'buds': 7}
]

pots = [
    {'id': 0, 'name': 'normal', 'timeAceleration': 0},
    {'id': 1, 'name': 'magic', 'timeAceleration': 0.5}
]

# https://hempire.fandom.com/

print('Categorias')
for category in categories:
    print('\t %d->%s' % (category['id'], category['name']))
print()

print('Cepas')
for strain in strains:

    idStrain = strain['id']

    if idStrain in [5, 6, 7]:
        nameStrain = strain['name'].upper()
        print('\n/// %s' % format(nameStrain))

    if idStrain == 5:
        # Test dictionary whit for bucle to get key and value
        for key, value in strain.items():
            print('{0} : {1} '.format(
                key, value), end='\t')
        print('\n//////')
        continue

    if idStrain == 6:
        # Test dictionary whit for bucle to get key and value
        for value in strain:
            print('{0} : {1} '.format(
                value, strain[value]), end='\t')
        print('\n//////')
        continue

    if idStrain == 7:
        # Test dictionary whit for bucle to get values
        for value in strain.values():
            print(value, end='\t')
        print('\n//////')
        continue

    if idStrain == 8:
        # Test to modify key value
        strain['category'] = 2
        print('Elementos: ', len(strain))

    if idStrain == 9:
        # Eliminar atributo con pop
        strain.pop("id")
        print(strain)

        # Eliminar atributo con del
        del strain["name"]
        print(strain)

        # Eliminar atributo con clear
        strain.clear()
        print(strain)
        continue

    print('\tCepa: {0}\t\tCategoria:{1}'.format(
          strain['name'], categories[strain['category']]['name']))
print()

print('Niveles de maestria para cepas disponibles:')
for mastery in strainMaestries:
    print('\tNivel: {0}, Cogollos Adicionales: {1}'.format(
        mastery['level'], mastery['buds'], end='\t'))

print()
print('Tipos de macetas:')
for pot in pots:
    print('\tTipo: {0}\tReducion de tiempo: {1}%'.format(
        pot['name'], int(pot['timeAceleration']*100)))


strains_bk = strains.copy()
print('My Strains count: %s' % len(strains_bk))

myStrain = []

for item in strains_bk:
    item.update({'count': 0})
    myStrain.append(item)

print(myStrain)
