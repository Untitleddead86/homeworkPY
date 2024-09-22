# 14_oop_telefon.py

"""
vytvořte 14_oop_telefon.py

vytvořte třídu MobilePhone

vymyslete k této třídě smysluplné atributy a metody
- 3-5 atributy (jaké vlastnosti a parametry by mohl mít mobilní telefon?)
- 2 metody (jaké chování (metody) by telefon mohl mít?)

vytvořte 2 instance
"""
class MobilePhone:
    def __init__(self, _id, name, group, os, display):
        self.id = _id
        self.name = name
        self.group = group
        self.os = os
        self.display = display

    def info(self):
        print(f"This is {self.name} {self.group} {self.os} {self.display}") # metody
       
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'os': self.os,
            'display': self.display,
        }
    
samsung = MobilePhone(1, 'Samsung', 'A60', 'android', 'amoled') # instance
xiaomi = MobilePhone(2, 'Xiaomi', '14', 'MI', 'amoled')
iphone = MobilePhone(3, 'IPhone', '14 Pro', 'OS', 'oled')

print(samsung.to_dict())
print(iphone.to_dict())



