import random

cities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok,Radom,Koniec Swiata,Paryż"
cities_list = cities.split(",")

numbers_list = list(range(0, 10, 1))
for i in range(0, 10):
    randomValue = random.choice(numbers_list)
    print(cities_list[randomValue])
    numbers_list.remove(randomValue)

