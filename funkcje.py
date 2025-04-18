# #deklaracja funkcji = utworzenie funkcji
# def fn():
#     print("test")
#
# #uzycie funkcji

# def add (a,b):
#     return a + b
#
# result1 = add(2,3)
# result2 = add(9,9)
# print(result1)
# print(result2)


# def multiply(x,y,z):
#     return x * y * z
# multi1 = multiply(1,2,3)
# multi2 = multiply(4,8,9)
#
# print(multi1)
# print(multi2)


# def checkPassword(password):
#     if len(password) <  6:
#         return False
#     else:
#         return True
# password_value = input("podaj swoje hasło: ")
# result = checkPassword(password_value)
#
# if result != True:
#     print("Twoje hasło jest za słabe")

# def user_info(name):
#     return "Cześć " + name +"!"
#
# user1 = user_info("Zbigniew")
# user2 = user_info("Anna")
#
# print(user1)
# print(user2)


#SŁOWNIK
# user = {
#     "firstname": "jan",
#     "lastname": "kowalsky",
#     "age": 30,
#     "address": {
#         "city": "Warszawa",
#         "street": "Krakowska"
#     }
# }
#
# lastname1 = user["lastname"]
# lastname2 = user.get("lastname")
# city = user["address"]["city"]
# street = user.get("address").get("street")
#
# user_keys = user.keys()
# user_values = user.values()
# user_items = user.items()
#
# print(user_keys)
# print(user_values)
# print(user_items)


