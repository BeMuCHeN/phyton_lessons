# 16-dars. Nesting.
"""
Created on Fri Sep  2 15:50:04 2022

author: Abror
"""

car01={'nom':'gentra','rang':'qora','yil':2016,'narx':12000}
car02={'nom':'nexia 3','rang':'oq','yil':2018,'narx':9000}
car03={'nom':'damas','rang':'oq','yil':2022,'narx':8500}

cars=[car01,car02,car03]
for car in cars:
    print(f"{car['nom'].title()} {car['rang']} rangli,"
          f" {car['yil']}-yilda ishlab chiqarilgan. Narxi:{car['narx']}$")