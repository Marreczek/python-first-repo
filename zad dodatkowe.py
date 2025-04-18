# #1
# try:
#     num = int(input("podaj liczbę: "))
#     if num % 2 == 0:
#         print("liczba jest parzysta")
#     else:
#         print("liczba jest nieparzysta")
# except ValueError:
#     print("To nie jest liczba! Spróbuj ponownie!")

# #2
# try:
#     age = int(input("ile masz lat? "))
#     if age >= 18:
#         print("Jesteś pełnoletni")
#     else:
#         print("Jesteś niepełnoletni")
# except ValueError:
#     print("podaj liczbę")

# #3
# while True:
#     try:
#         num_1 = int(input("podaj pierwszą liczbę: "))
#         num_2 = int(input("podaj drugą liczbę: "))
#         if num_1 == num_2:
#             print("Liczby są równe")
#         elif num_1 > num_2:
#             print("większa liczba to: ", num_1)
#         else:
#             print("większa liczba to: ", num_2)
#         break
#     except ValueError:
#         print("to nie jest liczba!")

# #4
# try:
#     point = int(input("podaj liczbę punktów (0-100)"))
#     if 0 <= point <=100:
#         if point >= 90:
#             print("ocena: A")
#         elif point >= 80:
#             print("ocena: B")
#         elif point >= 70:
#             print("ocena: C")
#         elif point >= 60:
#             print("ocena: D")
#         else:
#             print("ocena: F")
#     else:
#         print("błąd, wprowadź prawidłową liczbę punktów")
# except ValueError:
#     print("błąd, wprowadź liczbę całkowitą")

# #5
# try:
#     num = int(input("podaj liczbę całkowitą: "))
#     if num % 3 == 0 and num % 5 == 0:
#         print("liczba jest podzielna przez 3 i 5")
#     elif num % 3 == 0:
#         print("Liczba jest podzielna tylko przez 3.")
#     elif num % 5 == 0:
#         print("Liczba jest podzielna tylko przez 5.")
#     else:
#         print("liczba nie jest podzielna ani przez 3, ani przez 5")
# except ValueError:
#     print("Błąd. Wprowadzona wartość musi być liczbą całkowitą.")

#6
password = str(input("Podaj hasło: "))
if len(password) >= 8:
    print("hasło jest ok")
else:
    print("hasło jest za krótkie")