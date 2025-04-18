flights = [
    {'model': 'Embraer 190', 'passengers': 189, 'direction': 'Warszawa - Berlin', 'price': 300, 'departure_time': '11/04/2025, 06:50:00'},
    {'model': 'Boeing 777', 'passengers': 271, 'direction': 'Kraków - Londyn', 'price': 300, 'departure_time': '10/04/2025, 20:00:00'},
    {'model': 'Boeing 777', 'passengers': 261, 'direction': 'Poznań - Rzym', 'price': 550, 'departure_time': '10/04/2025, 16:10:00'},
    {'model': 'Embraer 190', 'passengers': 134, 'direction': 'Wrocław - Madryt', 'price': 700, 'departure_time': '10/04/2025, 13:45:00'},
    {'model': 'Embraer 190', 'passengers': 183, 'direction': 'Warszawa - Berlin', 'price': 450, 'departure_time': '10/04/2025, 13:45:00'},
    {'model': 'Boeing 737', 'passengers': 130, 'direction': 'Kraków - Londyn', 'price': 300, 'departure_time': '10/04/2025, 20:00:00'},
    {'model': 'Boeing 777', 'passengers': 245, 'direction': 'Kraków - Londyn', 'price': 550, 'departure_time': '10/04/2025, 16:10:00'},
    {'model': 'Boeing 777', 'passengers': 51, 'direction': 'Warszawa - Berlin', 'price': 700, 'departure_time': '10/04/2025, 13:45:00'},
    {'model': 'Embraer 190', 'passengers': 265, 'direction': 'Warszawa - Berlin', 'price': 150, 'departure_time': '10/04/2025, 16:10:00'},
    {'model': 'Boeing 737', 'passengers': 272, 'direction': 'Gdańsk - Paryż', 'price': 150, 'departure_time': '10/04/2025, 07:30:00'}
]

# 1. Użyj filter, aby wybrać loty, których cena przekracza 500 zł

price500 = list(filter(lambda x: x["price"] > 500, flights))
print(price500)

# 2. Użyj filter, aby wybrać loty, których data odlotu to 10 kwietnia 2025.
departure = list(filter(lambda x: x["departure_time"][:10] == "10/04/2025", flights))
print(departure)

# 3. Użyj filter, aby sprawdzić loty na kierunku Warszawa - Berlin
deutschland = list(filter(lambda x: x["direction"] == "Warszawa - Berlin", flights))
print(deutschland)

# 4. Użyj filter, aby sprawdzić loty na kierunku Kraków - Londyn, na których jest powyżej 250 pasażerów
crowded_flight = list(filter(lambda x: x["direction"] == "Kraków - Londyn" and x["passengers"] > 250, flights))
print(crowded_flight)

# 5. Użyj map, aby dla każdego lotu zwiększyć cenę o 20%.
inflation = list(map(lambda x: {**x, "price": x["price"] * 1.2}, flights))
print(inflation)

# 6. Użyj filter, aby wybrać tylko loty, które są obsługiwane przez samolot modelu "Boeing 777".
boink = list(filter(lambda x: x["model"] == "Boeing 777", flights))
print(boink)

# 7. Użyj map, aby z każdej podróży wyciągnąć tylko kierunek, czyli nazwę miasta docelowego.
destination = list(map(lambda x: x["direction"].split(" - ")[1], flights))
print(destination)

# 8. Przedstaw całkowitą liczbę pasażerów za pomocą metody reduce
from functools import reduce
total = reduce(lambda razem, x: razem + x["passengers"], flights, 0)
print(total)

# 9. Posortuj loty po ilości pasażerów (sort)


# 10. Przedstaw łączną kwotę jaką zarobiły linie lotnicze mnożąc ceny biletów przez wszystkich pasażerów  (reduce)

#dodatkowo - jak wyciągnąć unikalne wartości np model samolotu
airplanes = set(map(lambda x: x["model"], flights))
# airplanes_name = set(airplanes)
print(airplanes)


