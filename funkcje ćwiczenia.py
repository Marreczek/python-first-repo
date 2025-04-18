# # #1
# def multiply(a, b, c, d):
#     return a * b * c * d
#
# result = multiply(int(input("liczba 1. ")), int(input("liczba 2. ")), int(input("liczba 3. ")), int(input("liczba 4. ")))
#
# print(result)
#
#
#
# #2
# def triangle(a,h):
#     pole = (a * h) / 2
#     return pole
#
# a = float(input("Podaj podstawę: "))
# h = float(input("Podaj wysokość: "))
#
# wynik = triangle(a,h)
# print(f"Pole trójkąta wynosi {wynik}")
#
# #3
# def celsius_kelvin(kelvin):
#     celsius = kelvin - 273.15
#     return celsius
# kelvin = float(input("Podaj temperaturę w kelvinach: "))
# celsius = celsius_kelvin(kelvin)
# print(f"Temperatura w celsiuszach: {celsius}")

#4


#5
# from collections import Counter
#
# def analyze_text(text):
#     words = text.replace(",","").split()
#     total_words = len(words)
#     unique_words = len(set(words))
#     word_counts = Counter(words)
#     most_common = word_counts.most_common(1)[0][0]
#     longest_word_length = len(most_common)
#     return {
#         "total_words":total_words,
#         "unique_words": unique_words,
#         "most_common":most_common,
#         "longest_word_length": longest_word_length
#     }
#
# content = "To mój jest mój tekst, mój tekst nie może zawierać duplikatów"
# res = analyze_text(content)
# print(res)

#1 z funkcją lambda
mnoz_cztery = lambda a, b, c, d: a * b * c * d
res = mnoz_cztery(1,2,3,4)
print(res)

#2 z lambda
triangle = lambda a, h: (a * h) / 2
res2 = triangle(4,4)
print(res2)

#3
celsius_kelvin = lambda num: num - 273
res3 = celsius_kelvin(100)
print(res3)