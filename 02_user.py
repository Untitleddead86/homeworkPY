# 02_user.py

"""
2) vytvořte 02_user.py kde
uživatel zadá své jmeno a věk pomocí input
uložte tyto informace do souboru
02_user.txt
"""

jmeno = input('Zadej jmeno: ')
vek = input('Zadej vek: ')

with open("02_user.txt", "+a") as file:
    file.write(jmeno + ", " + vek + "\n")