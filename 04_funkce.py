# 04_funkce.py

"""
Vytvořte soubor 04_funkce.py

ve kterém budou 2 funkce:

1) funkce pro výpočet obsahu kruhu s = pr**r
2) funkce pro vpočet obvodu kruhu  s = 2pr

vstupní parametr bude poloměr
 
Viz zde:
https://www.umimeto.org/asset/system/um/img/rules/ilustrace-obsah-obvod-prehled.png


řecké písmeno PI definujte jako 3.14 nebo importujte modul math, kde se nachází konstanta pi

import math

print(math.pi)

obě funkce otestujte
"""
import math

print(round(math.pi, 2))

polomer = float(input('zadejte polomer: '))


def obsah_kruhu():
    S = math.pi * polomer ** 2
    print(round(S, 2))
   

def obvod_kruhu():
    O = 2 *  math.pi * polomer 
    return round(O, 2)
    

obsah_kruhu()
print(obvod_kruhu())

