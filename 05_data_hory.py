# data_hory.py
"""
vytvořte soubor 05_for_cyklus.py

v listu lze zapsat data i takto pod sebe:

kde budou data = [
    8848, # Mount Everest
    8611, # K2
    4808, # Mont Blanc
    5895, # Kilimanjaro
    3776, # Mount Fuji
    5642, # Elbrus
    1603, # Sněžka
    1492, # Praděd
    1323, # Lysá hora
]

logika bude následující:
for cyklem projděte všechny nadmořské výšky a pokud:
je hora nižší jak 3000 m - napište X je nizká výška
je hora 3000 m a více, ale zároveň méně jak 6000 m - napište X je střední výška
jinak napište X je vysoká výška
.. kde X je výška
"""

data = [
    8848, 'Mount Everest',
    8611, 'K2',
    4808, 'Mont Blanc',
    5895, 'Kilimanjaro',
    3776, 'Mount Fuji',
    5642, 'Elbrus',
    1603, 'Sněžka',
    1492, 'Praděd',
    1323, 'Lysá hora'
]

for i in range(0, len(data), 2):
    vyska = data[i]
    hora = data[i + 1]
    if vyska < 3000: 
        print(f'{vyska} {hora} je nizka vyska')

    elif 3000 <= vyska < 6000:
        print(f'{vyska} {hora} je stredni vyska')

    else:
        print(f'{vyska} {hora} je vysoka vyska')