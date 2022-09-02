from audioop import reverse
from operator import length_hint


X = 1
Y = 4
addresses = {"Karl": "A Klockgatan 1",
             "Adam": "B Ormvägen 5",
             "Cornelia": "C Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

#print(f'Bellas Adress: {addresses["Bella"]}')

addresses["Göran"] = "D Prinsgränd 2"

#print(len(addresses))
"""
last_place = sorted(addresses, key=None, reverse=True)

for x in addresses:
    if(x == last_place[0]):
        print(last_place[0],addresses[x])
    else:
        print(addresses[x])

first_place = sorted(addresses, key=None, reverse=False)
print(first_place)
k = first_place
new_dict: addresses={v:k for k, v in addresses.items()}
"""

cars.sort()

cars_2 = cars
cars.append("Saab")
cars_3 = frozenset(cars)

#for x in range(len(cars)):      #Not needed, extend did the same thing
#    cars.append(cars[x])

cars.extend(cars)
cars = sorted(cars,key=str,reverse=True)

print(cars)

unique_cars = set(cars)

print(unique_cars)
