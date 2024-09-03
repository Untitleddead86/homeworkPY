# 09_dict.staty.py

"""
vytvořte soubor 09_dict_staty.py

kde budou data:

staty = {
    'CZ': 'Česko',
    'SK': 'Slovensko',
    'PL': 'Polsko',
    'DE': 'Německo',
    'AT': 'Rakousko',
}

Pomocí kódu udělejte:
1. pridejte do statů nový klíč 'HU' s hodnotou 'Maďarsko'
2. vytvořte nové dict staty_delka
do kterého pomocí for cyklu přidáte pro každý klíč, délku názvu státu
3. udělete printy pro kontrolu změn

výsledek tedy bude:
staty_delka = {
    'CZ': 6,
    'SK': 9,
    'PL': 6,
    'DE': 7,
    'AT': 8,
    'HU': 8,
}
"""

staty = {
    'CZ': 'Česko',
    'SK': 'Slovensko',
    'PL': 'Polsko',
    'DE': 'Německo',
    'AT': 'Rakousko',
}


staty["HU"] = "Madarsko"

print(staty)

staty_delka = {}

for key in staty:
    count = len(staty[key])
    staty_delka[key] = count
    print(key, staty_delka[key])
    
    







 
