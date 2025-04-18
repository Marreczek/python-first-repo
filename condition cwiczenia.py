#1
user_role = "admin"
is_logged = True

if user_role == "admin" and is_logged == True:
    print("Witaj w panelu admina")
elif user_role == "mod" and is_logged == True:
    print("Witaj w panelu moderatora")
elif user_role == "user" and is_logged == True:
    print("Witaj w panelu użytkownika")
else:
    print("błąd logowania")

#2
user_country = "Polska"
if user_country == "Polska" or user_country == "Niemcy" or user_country == "Czechy":
    print("Złóż zamówienie")
else:
    print("Dostawa towaru niemożliwa")

#3
hour = 8
if hour >= 6 and hour < 12:
    print("Good morning")
elif hour >= 12 and hour < 18:
    print("Good afternoon")
elif hour > 18:
    print("Good evening")
else:
    print("inna")

#3 v2
from datetime import datetime
current_time = datetime.now().hour
if 6 <= current_time < 12:
    print("Good Morning")
elif 12 <= current_time < 18:
    print("Good Afternoon")
else:
    print("Good Evening")

