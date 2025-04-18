#1
#Napisz pętlę, która w princie dźwiga liczbę do potęgi drugiej, jeśli jest parzysta
nums = [12,7,4,3,2,8,9]
for num in nums:
    if num % 2 == 0:
        print(num ** 2)

#2
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#3 Napisz program, który obliczy sumę wszystkich liczb parzystych od 1 do podanej liczby n (włącznie).
# - w inpucie podajemy liczbę, konwertujemy - potem pętla np. range

try:
    n = int(input("Podaj liczbę: "))
    sum = 0
    for i in range(1,n + 1):
        if i % 2 == 0:
            sum += i
    print(f"Suma liczb parzystych od 1 do {n} wynosi:", sum)

except ValueError:
    print("błąd! Podaj poprawną liczbę!")

# 4. Poproś użytkownika o wpisanie słowa i wypisz je za pomocą petli w odwrotnej kolejności,
# znak po znaku (nie używaj [::-1])

word = input("Podaj słowo: ")
for i in range(len(word) -1, -1, -1):
    print(word[i])
