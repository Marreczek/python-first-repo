#1
grade = input("Podaj ocenę (1-6)")
match grade:
    case "1":
        print("1 - niedostateczny")
    case "2":
        print("2 - dopuszczający")
    case "3":
        print("3 - dostateczny")
    case "4":
        print("4 - dobry")
    case "5":
        print("5 - bardzo dobry")
    case "6":
        print("6 - celujący")
    case _:
        print("Ocena nieprawidłowa. Podaj ocenę z przedziału od 1 do 6")

#2 z czatu gpt  - nie działa
name = input("podaj nazwę użytkownika: ")
name = name.replace(" ","")
try:
    if name.isalpha() and len(name) >= 5:
            print("Nazwa użytkownika jest poprawna.")
    else:
            print("Błędna nazwa")
except Exception as e:
        print(f"Błąd: {e}")
