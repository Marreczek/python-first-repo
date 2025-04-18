# # cities = ["Warszawa", "Kraków", "Ełk", "Wrocław", "Poznań"]
# # new_cities = ["London", "Berlin"]
# #
# # last = cities[-1] #zwraca ostatni element
# # print(last)
# #
# # last2 = cities[len(cities)-1] #len zwraca długość kolekcji
# # print(last2)
# #
# # cities.append("Szczecin") # dodaje nowy element do listy
# # cities.extend(new_cities) #rozszerza liste o elementy z innej listy
# #
# # print(cities)
# #
# # cities.insert(1, "Katowice") # dodaj element pod indeksem 1
# # cities.remove("Ełk") # usuwa element
# # cities.sort() # sortuje alfabetycznie
# # cities.sort(reverse=True) #sortuje odwrotnie alfabetycznie
# # cities.pop() #usuwa i zwraca usuniety element
# # cities.reverse() #odwraca kolejność
# # print(cities)
# #
# #
# # values = [
# #     [5,7],
# #     [1,8],
# #     [4,6]
# # ]
# # #rzadko wykorzystamy macierz
# # print(values[1][1]) #druga liczba z drugiej listy
# from numbers import result
#
#
# # nums = [1,2,3,4,5,6,7,]
# # # new_list = []
# # # for num in nums:
# # #     res = num * num
# # #     new_list.append(res)
# # #
# # # print(new_list)
# #
# # multiply = map(lambda x: x * x, nums)
# # print(list(multiply))
# # # map
#
# # users = ["Kasia", "Kazimierz", "Jan", "John", "Władysław"]
#
# # short_names = []    #wyciąga imiona krótsze niz 5 liter
# # for user in users:
# #     if len(user) > 5:
# #         continue
# #     else:
# #         short_names.append(user)
# #
# # short_names = list(filter(lambda x: len(x) < 5, users))
# # print(users)
# # print(short_names)
#
# # map_users= list(map(lambda x: f"To jest {x}", users))
# # print(map_users)
# #
# # def change_user(x):
# #     return f"To jest {x}"
#
# # users2 = list(map(change_user, users))
# # print(users2)
#
#
#
# # users = [
# #     {"imie": "Anna", "miasto": "Warszawa", "wiek": 38},
# #     {"imie": "Jan", "miasto": "Kraków", "wiek": 27},
# #     {"imie": "Maria", "miasto": "Gdańsk", "wiek": 45},
# #     {"imie": "Tomasz", "miasto": "Poznań", "wiek": 32},
# #     {"imie": "Katarzyna", "miasto": "Wrocław", "wiek": 29},
# #     {"imie": "Piotr", "miasto": "Szczecin", "wiek": 41},
# #     {"imie": "Agnieszka", "miasto": "Lublin", "wiek": 35},
# #     {"imie": "Michał", "miasto": "Bydgoszcz", "wiek": 23},
# #     {"imie": "Ewa", "miasto": "Rzeszów", "wiek": 30},
# #     {"imie": "Paweł", "miasto": "Katowice", "wiek": 39}
# # ]
# #
# # # current_city = list(filter(lambda x: x["miasto"] == "Kraków", users))
# # # above30 = list(filter(lambda a: a["wiek"] > 30, users))
# # #
# # # cities2 = list(filter(lambda x: x["miasto"] == "Warszawa" and x["wiek"] >=30, users))
# # # print(cities2)
# #
# # uppercase = list(map(lambda x: {
# #     **x,
# #     "miasto": x["miasto"].upper()
# # }, users))
# # print(uppercase)
# #
#
#
# # def test():
# #     print("testowa")
# #
# # def start(fn):
# #     fn()
# #
# # start(test)
#
# FILTROWANIE
def filtrowanie(fn, collection):
    result = []

    for item in collection:
        if fn(item) == True: #jeśli ten item jest true dodawaj go do nowej tablicy
            result.append(item)

    return result

nums = [ 4, 7, 8, 9, 3, 1, 1, 2, 9]
filtered = filtrowanie(lambda x: x > 4, nums)
modulo = filtrowanie(lambda x: x % 3 == 0, nums)

print(filtered)
print(modulo)


def mapowanie(fn, collection):
    result = []
    for item in collection:
        value = fn(item)
        result.append(value)
    return result

power = mapowanie(lambda x: x**2, nums)
power2 = list(map(lambda x: x**2, nums))