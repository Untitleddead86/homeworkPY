# 13_oop.py

"""
3. vytvořte soubor 13_oop.py
a v něm třídu Planeta, která bude obsahovat:
atributy:
- poradi 
- nazev

a metodu info
která řekne "Toto je [název planety] a je [pořadí] od Slunce"

vytvořte 2 instance
- Země
- a nějakou další planetu
"""

class Planet:
    def __init__(self, name, order):
        self.name = name
        self.order = order
        

    def info(self):
        print(f"This is {self.name} and order of {self.order}-th from Sun.")

earth = Planet("Earth", 3)
earth.info()

merkury = Planet("Merkury", 1)
merkury.info()

venus = Planet("Venus", 2)
venus.info()

