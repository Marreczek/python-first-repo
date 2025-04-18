#1
lista = []
lista.append(8)
lista.append(7)
lista.append(6)
print(lista)

#2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#3
my_list = [1, 2, 3, 4, 2]
my_list.remove(2)
my_list.pop()

print(my_list)

#4
my_list2 = [10, 20, 40, 30, 20]
index40 = my_list2.index(40)
print(index40)

#5
my_list3 = [1, 2, 2, 3, 2, 4, 2]
counter = my_list3.count(2)
print(counter)

#6
def rotate_list(lst, k):
    if not lst:
        return lst  # Zwróć pustą listę, jeśli wejście jest puste

    k = k % len(lst)  # Użycie modulo, by uniknąć nadmiarowego przesunięcia
    return lst[-k:] + lst[:-k]
lista = [1, 2, 3, 4, 5]
wynik = rotate_list(lista, 2)
print(wynik)
