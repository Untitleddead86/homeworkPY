# 07_mesta.py
"""
soubor se bude jmenovat 07_mesta.py

máme tato data se sloupci
1. nazev
2. pocet_obyvatel
3. rozloha

eu_cities = [
    ['Berlín', 3669491, 891],
    ['Madrid', 3223334, 604],
    ['Řím', 2872800, 1285],
    ['Paříž', 2165423, 105],
    ['Bukurešť', 1883425, 228],
    ['Budapešť', 1746344, 525],
    ['Varšava', 1790658, 517],
    ['Vídeň', 1921153, 414],
    ['Hamburk', 1841179, 755],
    ['Barcelona', 1620343, 101]
]

pomocí for cyklu zjistěte:
1) jaký je celkový počet obyvatel v těchto městech
2) které město má nejvíce a nejměně obyvatel
"""

eu_cities = [
    ['Berlín', 3669491, 891],
    ['Madrid', 3223334, 604],
    ['Řím', 2872800, 1285],
    ['Paříž', 2165423, 105],
    ['Bukurešť', 1883425, 228],
    ['Budapešť', 1746344, 525],
    ['Varšava', 1790658, 517],
    ['Vídeň', 1921153, 414],
    ['Hamburk', 1841179, 755],
    ['Barcelona', 1620343, 101],
]


number_of_residents = 0

min_city = ""
max_city = ""
max_residents = 0
min_residents = 1_000_000_000

for city, residents, square in eu_cities:
    number_of_residents = residents + number_of_residents

print(f'Sum of citizens EU: {number_of_residents} \n')



for i in eu_cities:
    if i[1] > max_residents:
        max_residents = i[1]
        max_city = i[0]
    if i[1] < min_residents:
        min_residents = i[1]
        min_city = i[0]

print(f'Max population is: {max_residents} in {max_city}\n')
print(f'Min population is: {min_residents} in {min_city}')



