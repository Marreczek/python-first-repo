# licznik = 0
# while licznik < 5:
#     print("wartość licznika:", licznik)
#     licznik += 1

import random
#from nis import match

# num = 0
# while num != 7:
#     num = random.randint(0,20)
#     print("wylosowano liczbę",num)
#
# #pętla nieskończona - przy pętli while, wykonuj tyle razy ile spełniony będzie warunek
# counter = 1
# while counter <10:
#     print("pętla wykonana", counter)
#     counter += 1

# import random
# num = 0
# iters = 0
# while num != 7:
#     if iters >= 4000:
#         print("nie udało się znaleźć liczby")
#         break
#     iters += 1
#     num = random.randint(0,5000)
#     print(f"Iteracja {iters}. Wylosowano liczbę {num}")


# test = "jan kowalski"
# for l in test:
#     if l == "w":
#         break
#     print(l)


# while True:
#     print("1. inf o koncie")
#     print("2. wpłać pieniądze")
#     print("3. zamknij program")
#     operation = input("wybierz operację:")
#
#     match operation:
#         case "1":
#             print("Panel użytkownika....")
#         case "2":
#             print("Wpłacam 1000 zł")
#         case "3":
#             print("Do zobaczenia")
#             break


for num in range(1, 200):
    if num % 5 == 0:
        continue
    print(num)