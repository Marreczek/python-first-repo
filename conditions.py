# bool / boolean - zwraca prawdę albo fałsz, nie może przyjąć inych wartości
#zwraca np większe, większe lub równe, mniejsze itp
#== oznacza porównanie

is_true = True
is_false = False

num = 5
if num > 5:
    print("masz rację")
    print("liczba jest większa")
else:
    print("warunek nie został spełniony")


account = "mod"
if account == "admin":
    print("witamy admina")
elif account == "mod":
    print("witaj moderatorze")
elif account == "user":
    print("witaj użyszkodniku")
else:
    print("nie rozpoznano")



email = input("Podaj email")

if email:
    print("działa")

user_country = "Finlandia"
price = 100

match user_country:
    case "Polska" | "Finlandia":
        price *= 1.23
    case "Francja":
        price *= 1.18
    case "Niemcy":
        price *= 1.20
    case _:
        price *= 1.10

print(f"Do zapłaty {price}")
