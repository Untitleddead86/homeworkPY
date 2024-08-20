""" 
vytvořte script, který zjistí jestli je věk teenager nebo ne:
teenager je od 13-19 let

uživatel zadá číslo (věk)

pokud je teenager, vypíše "jsi teenager"
jinak "nejsi teenager"

vytvořte nový repozitář nebo nahrajte existujícího repozitáře

jako test_teenager.py
"""


vek = input('Zadej svuj vek: ')
vek = int(vek)

if vek >= 13 and vek <= 19:
    print('Jsi teenager')
else:
    print('Nejsi teenager')
