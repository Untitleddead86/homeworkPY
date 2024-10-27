# 16_animal.py
"""
vytvořte 16_animal.py a v něm:

- obecou trídu Animal, která bude mít v init name jako privátní proměnou

- třída Dog - pro metodu sound() - bude printovat jméno + "wof"
- třída Cat - pro metodu sound() - bude printovat jméno + "mňau"


příklad použití:
my_dog = Dog('Stark')
my_dog.sound() # printuje 'Stark: Wof'

my_cat = Cat('Dizzy')
my_cat.sound() # printuje 'Dizzy: mňau'

name v bude v obou případech dostupné přes ._name
= privátní attribut/proměnná

my_dog._name
my_cat._name
"""

class Animal:
    def __init__(self,name):
        self.name = name
    
class Dog(Animal):
    def sound(self):
       
        print(f"{self.name} + Wof")

my_dog = Dog("Snuppy")
my_dog.sound()

class Cat:
    def sound(self):
        
        print(f"{self.name} + miau")

my_cat = Cat("Mad")
my_cat.sound()