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

for i in data:
    if i < 3000: 
        print(i, 'Je nizka vyska')

    elif 3000 < i < 6000:
        print(i, 'Je stredni vyska')

    else:
        print("Je vysoka vyska")